from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.user import UserModel
from security.password import hash_password, verify_password


def register_user(db: Session, email: str, password: str):
    # Check if user already exists
    existing_user = db.query(UserModel).filter(
        UserModel.email == email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # Hash password
    hashed_password = hash_password(password)

    # Create user
    new_user = UserModel(
        email=email,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(db: Session, email: str, password: str):
    # find user by email
    user = db.query(UserModel).filter(
        UserModel.email == email
    ).first()

    # User not found
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Verify password
    if not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return user