import logging
from email.message import EmailMessage

import aiosmtplib

from app.core.config import settings


logger = logging.getLogger(__name__)


async def send_otp_email(
    recipient: str,
    otp: str,
) -> None:
    """
    Send an OTP email.

    In development, when SMTP is not configured,
    the OTP is printed in the backend terminal.
    """

    if not settings.SMTP_HOST or not settings.SMTP_FROM_EMAIL:
        logger.warning(
            "SMTP is not configured. Development OTP for %s: %s",
            recipient,
            otp,
        )
        print(f"\n[DEV OTP] {recipient}: {otp}\n")
        return

    message = EmailMessage()
    message["From"] = settings.SMTP_FROM_EMAIL
    message["To"] = recipient
    message["Subject"] = "InsightHub AI - Verification OTP"

    message.set_content(
        f"""
Hello,

Your InsightHub AI verification code is:

{otp}

This OTP will expire in 5 minutes.

If you did not request this verification,
you can ignore this email.

InsightHub AI
""".strip()
    )

    await aiosmtplib.send(
        message,
        hostname=settings.SMTP_HOST,
        port=settings.SMTP_PORT,
        username=settings.SMTP_USERNAME or None,
        password=settings.SMTP_PASSWORD or None,
        start_tls=settings.SMTP_USE_TLS,
    )