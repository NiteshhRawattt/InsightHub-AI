import uuid
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, model_validator


class SignupRequest(BaseModel):
    email: EmailStr | None = None
    phone: str | None = Field(default=None, min_length=8, max_length=20)
    password: str = Field(min_length=8, max_length=128)
    full_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=150,
    )

    @model_validator(mode="after")
    def validate_identifier(self):
        if not self.email and not self.phone:
            raise ValueError("Email or phone number is required")

        if self.email and self.phone:
            raise ValueError(
                "Provide either email or phone number, not both"
            )

        return self


class VerifyOTPRequest(BaseModel):
    email: EmailStr | None = None
    phone: str | None = Field(default=None, min_length=8, max_length=20)
    otp: str = Field(pattern=r"^\d{6}$")

    @model_validator(mode="after")
    def validate_identifier(self):
        if not self.email and not self.phone:
            raise ValueError("Email or phone number is required")

        if self.email and self.phone:
            raise ValueError(
                "Provide either email or phone number, not both"
            )

        return self


class LoginRequest(BaseModel):
    email: EmailStr | None = None
    phone: str | None = Field(default=None, min_length=8, max_length=20)
    password: str = Field(min_length=8, max_length=128)

    @model_validator(mode="after")
    def validate_identifier(self):
        if not self.email and not self.phone:
            raise ValueError("Email or phone number is required")

        if self.email and self.phone:
            raise ValueError(
                "Provide either email or phone number, not both"
            )

        return self


class ResendOTPRequest(BaseModel):
    email: EmailStr | None = None
    phone: str | None = Field(default=None, min_length=8, max_length=20)

    @model_validator(mode="after")
    def validate_identifier(self):
        if not self.email and not self.phone:
            raise ValueError("Email or phone number is required")

        if self.email and self.phone:
            raise ValueError(
                "Provide either email or phone number, not both"
            )

        return self


class RefreshTokenRequest(BaseModel):
    refresh_token: str = Field(min_length=1)


class UserResponse(BaseModel):
    id: uuid.UUID
    email: EmailStr | None = None
    phone: str | None = None
    full_name: str | None = None
    is_verified: bool
    is_active: bool
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }


class MessageResponse(BaseModel):
    message: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: UserResponse