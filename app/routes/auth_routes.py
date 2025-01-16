from fastapi import APIRouter, HTTPException
from app.schemas.auth_schema import AuthSchema
from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.services.auth_service import hash_password, verify_password
from app.config.database import get_db
from app.schemas.user_schema import UserCreate, UserResponse
from sqlalchemy.orm import Session
from app.models import User

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user by hashing and storing their password.
    """
    # Check if username or email already exists
    existing_user = db.query(User).filter((User.username == user.username) | (User.email == user.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already exists.")

    # Hash the user's password
    hashed_password = hash_password(user.password)

    # Create a new user instance
    new_user = User(username=user.username, email=user.email, hashed_password=hashed_password)

    # Add to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Authenticate the user by validating their password and return a token.
    """
    # Fetch user from database
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # Verify the password
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # Return token (use JWT in production)
    return {"access_token": user.username, "token_type": "bearer"}
    