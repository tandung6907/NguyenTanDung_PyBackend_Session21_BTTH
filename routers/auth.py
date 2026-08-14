from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services.auth import register_user, login_user
from schemas.auth import (
    RegisterInput,
    LoginInput,
    AuthResponse
)
from security.jwt import create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post(
    "/register",
    response_model= AuthResponse,
    status_code= 201
)
def register(
    data: RegisterInput,
    db: Session = Depends(get_db)
):
    user = register_user(
        db,
        data.email,
        data.password
    )

    access_token = create_access_token({
        "sub": user.email
    })

    return AuthResponse(
        access_token= access_token
    )


@router.post(
    "/login",
    response_model= AuthResponse
)
def login(
    data: LoginInput,
    db: Session = Depends(get_db)
):
    user = login_user(
        db,
        data.email,
        data.password
    )

    access_token = create_access_token({
        "sub": user.email
    })

    return AuthResponse(
        access_token= access_token
    )