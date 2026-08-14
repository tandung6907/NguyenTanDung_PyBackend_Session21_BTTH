from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.user import UserModel
from security.password import hash_password


def register_user(db: Session, email: str, password: str):
    # Check if the user already exists
    existing_user = db.query(UserModel).filter(UserModel.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password
    hashed_password = hash_password(password)

    # Create a new user instance
    new_user = UserModel(email=email, hashed_password=hashed_password)

    # Add the new user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user