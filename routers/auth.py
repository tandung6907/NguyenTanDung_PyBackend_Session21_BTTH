from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.auth import register_user
from schemas.auth import AuthResponse
from security.jwt import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register", response_model= AuthResponse, status_code= 201)
def register(db: Session = Depends(get_db), email: str = None, password: str = None):
    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and password are required")

    user = register_user(db, email, password)

    # Generate access token
    access_token = create_access_token({"sub": user.email})

    return AuthResponse(access_token= access_token)