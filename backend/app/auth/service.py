import hashlib
from datetime import datetime, timedelta, timezone

from fastapi import HTTPException, status
from sqlalchemy import or_, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.auth.email import send_otp_email
from app.auth.models import OTP, RefreshToken, User
from app.auth.otp import (
    generate_otp,
    get_otp_expiry,
    hash_otp,
    is_otp_expired,
    verify_otp,
)
from app.auth.schemas import (
    LoginRequest,
    SignupRequest,
    TokenResponse,
    VerifyOTPRequest,
)
from app.auth.security import hash_password, verify_password

from app.auth.jwt import create_access_token, create_refresh_token
from app.core.config import settings

def get_user_by_email(
    db: Session,
    email: str,
) -> User | None:
    statement = select(User).where(User.email == email)

    return db.scalars(statement).first()


def get_user_by_phone(
    db: Session,
    phone: str,
) -> User | None:
    statement = select(User).where(User.phone == phone)

    return db.scalars(statement).first()


def get_user_by_identifier(
    db: Session,
    email: str | None = None,
    phone: str | None = None,
) -> User | None:
    conditions = []

    if email:
        conditions.append(User.email == email)

    if phone:
        conditions.append(User.phone == phone)

    if not conditions:
        return None

    statement = select(User).where(or_(*conditions))

    return db.scalars(statement).first()


def invalidate_existing_otps(
    db: Session,
    user_id,
    purpose: str,
) -> None:
    """
    Mark all previous unused OTPs for the same purpose as used.
    """

    statement = select(OTP).where(
        OTP.user_id == user_id,
        OTP.purpose == purpose,
        OTP.is_used.is_(False),
    )

    existing_otps = db.scalars(statement).all()

    for otp_record in existing_otps:
        otp_record.is_used = True


async def signup_user(
    db: Session,
    payload: SignupRequest,
) -> User:
    """
    Register a new user and create a verification OTP.
    """

    existing_user = get_user_by_identifier(
        db=db,
        email=payload.email,
        phone=payload.phone,
    )

    if existing_user:
        if existing_user.is_verified:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="An account with this email or phone already exists.",
            )

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "An unverified account already exists. "
                "Please verify the account or request a new OTP."
            ),
        )

    user = User(
        email=payload.email,
        phone=payload.phone,
        full_name=payload.full_name,
        password_hash=hash_password(payload.password),
        is_verified=False,
        is_active=True,
    )

    try:
        db.add(user)
        db.flush()

        plain_otp = generate_otp()

        otp_record = OTP(
            user_id=user.id,
            otp_hash=hash_otp(plain_otp),
            purpose="signup_verification",
            channel="email" if payload.email else "sms",
            expires_at=get_otp_expiry(),
            is_used=False,
            attempts=0,
            created_at=datetime.now(timezone.utc),
        )

        db.add(otp_record)
        db.commit()
        db.refresh(user)

    except IntegrityError as exc:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account with this email or phone already exists.",
        ) from exc

    except Exception:
        db.rollback()
        raise

    if payload.email:
        await send_otp_email(
            recipient=payload.email,
            otp=plain_otp,
        )

    else:
        # SMS integration will be added later.
        print(f"\n[DEV OTP] {payload.phone}: {plain_otp}\n")

    return user

async def verify_signup_otp(
    db: Session,
    payload: VerifyOTPRequest,
) -> User:
    """
    Verify the latest signup OTP and activate the user account.
    """

    user = get_user_by_identifier(
        db=db,
        email=payload.email,
        phone=payload.phone,
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User account not found.",
        )

    if user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Account is already verified.",
        )

    statement = (
        select(OTP)
        .where(
            OTP.user_id == user.id,
            OTP.purpose == "signup_verification",
            OTP.is_used.is_(False),
        )
        .order_by(OTP.created_at.desc())
    )

    otp_record = db.scalars(statement).first()

    if not otp_record:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No active OTP found. Please request a new OTP.",
        )

    if is_otp_expired(otp_record.expires_at):
        otp_record.is_used = True
        db.commit()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="OTP has expired. Please request a new OTP.",
        )

    if otp_record.attempts >= 5:
        otp_record.is_used = True
        db.commit()

        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Maximum OTP attempts exceeded. Please request a new OTP.",
        )

    if not verify_otp(
        plain_otp=payload.otp,
        stored_hash=otp_record.otp_hash,
    ):
        otp_record.attempts += 1
        db.commit()

        remaining_attempts = max(
            0,
            5 - otp_record.attempts,
        )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid OTP. {remaining_attempts} attempts remaining.",
        )

    try:
        otp_record.is_used = True
        user.is_verified = True

        db.commit()
        db.refresh(user)

    except Exception:
        db.rollback()
        raise

    return user

def hash_refresh_token(token: str) -> str:
    """
    Hash refresh token before storing it in the database.
    """

    return hashlib.sha256(
        token.encode("utf-8")
    ).hexdigest()

async def login_user(
    db: Session,
    payload: LoginRequest,
) -> TokenResponse:
    """
    Authenticate a user and issue access and refresh tokens.
    """

    user = get_user_by_identifier(
        db=db,
        email=payload.email,
        phone=payload.phone,
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email, phone number, or password.",
        )

    if not verify_password(
        plain_password=payload.password,
        hashed_password=user.password_hash,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email, phone number, or password.",
        )

    if not user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is not verified. Please verify your OTP first.",
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is inactive.",
        )

    access_token = create_access_token(
        subject=str(user.id),
    )

    refresh_token = create_refresh_token(
        subject=str(user.id),
    )

    refresh_token_record = RefreshToken(
        user_id=user.id,
        token_hash=hash_refresh_token(refresh_token),
        expires_at=datetime.now(timezone.utc)
        + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
        is_revoked=False,
        created_at=datetime.now(timezone.utc),
    )

    try:
        db.add(refresh_token_record)
        db.commit()

    except Exception:
        db.rollback()
        raise

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        user=user,
    )