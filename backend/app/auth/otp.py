import hashlib
import hmac
import secrets
from datetime import datetime, timedelta, timezone

from app.core.config import settings


OTP_LENGTH = 6
OTP_EXPIRE_MINUTES = 5


def generate_otp() -> str:
    """
    Generate a secure 6-digit OTP.
    """

    minimum = 10 ** (OTP_LENGTH - 1)
    maximum = 10**OTP_LENGTH

    return str(
        minimum + secrets.randbelow(maximum - minimum)
    )


def hash_otp(otp: str) -> str:
    """
    Hash OTP before storing it in the database.
    """

    value = f"{otp}:{settings.JWT_SECRET_KEY}"

    return hashlib.sha256(
        value.encode("utf-8")
    ).hexdigest()


def verify_otp(
    plain_otp: str,
    stored_hash: str,
) -> bool:
    """
    Compare a plain OTP with the stored OTP hash.
    """

    calculated_hash = hash_otp(plain_otp)

    return hmac.compare_digest(
        calculated_hash,
        stored_hash,
    )


def get_otp_expiry() -> datetime:
    """
    Return the OTP expiry datetime.
    """

    return datetime.now(timezone.utc) + timedelta(
        minutes=OTP_EXPIRE_MINUTES
    )


def is_otp_expired(expires_at: datetime) -> bool:
    """
    Check whether an OTP has expired.
    """

    return datetime.now(timezone.utc) >= expires_at