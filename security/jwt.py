import os
import jwt
from dotenv import load_dotenv
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timedelta, timezone


load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
MINUTES = 30


def create_access_token(payload: dict):
    to_encode = payload.copy()

    expires_time = datetime.now(timezone.utc) + timedelta(minutes=MINUTES)

    to_encode.update({
        "exp": expires_time
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


def verify_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except ExpiredSignatureError:
        raise Exception("Token has expired")

    except InvalidTokenError:
        raise Exception("Invalid token")