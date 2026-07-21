from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_db
from app.auth.schemas import (
    SignupRequest,
    UserResponse,
    VerifyOTPRequest,
)
from app.auth.service import signup_user, verify_signup_otp


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

DatabaseSession = Annotated[Session, Depends(get_db)]


@router.post(
    "/signup",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user account",
)
async def signup(
    payload: SignupRequest,
    db: DatabaseSession,
) -> UserResponse:
    """
    Register a user using either an email address or phone number.

    A six-digit OTP is generated after successful registration.
    """

    user = await signup_user(
        db=db,
        payload=payload,
    )

    return UserResponse.model_validate(user)

@router.post(
    "/verify-otp",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Verify signup OTP",
)
async def verify_otp_endpoint(
    payload: VerifyOTPRequest,
    db: DatabaseSession,
) -> UserResponse:
    """
    Verify the OTP generated during signup.
    """

    user = await verify_signup_otp(
        db=db,
        payload=payload,
    )

    return UserResponse.model_validate(user)