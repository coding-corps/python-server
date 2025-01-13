from app.models.user_model import User
from passlib.context import CryptContext
from fastapi import HTTPException
from datetime import datetime, timedelta
from typing import Optional
import jwt
import os

# Assuming these values come from your settings (from .env or settings file)
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt_secret_key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# Initialize the CryptContext for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(data):
    # Hash the password before saving the user
    hashed_password = get_password_hash(data["password"])  # Use passlib to hash password
    user = User(username=data["username"], password=hashed_password)
    user.save()  # Ensure `save()` properly handles database persistence
    return {"message": "User registered successfully"}

def login_user(data):
    # Look for user in the database using username
    user = User.query.filter_by(username=data["username"]).first()
    
    # Validate user existence and password match
    if not user or not verify_password(data["password"], user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Return login success message
    return {"message": "Login successful"}

# Create JWT token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    # Encode the JWT with the secret key and algorithm
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Decode JWT token and verify its validity
def decode_access_token(token: str):
    try:
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

# Verify password hash using passlib context
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# Hash password using passlib context
def get_password_hash(password: str):
    return pwd_context.hash(password)
