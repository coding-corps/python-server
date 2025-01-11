from app.models.user_model import User
from werkzeug.security import generate_password_hash, check_password_hash

def register_user(data):
    hashed_password = generate_password_hash(data["password"])
    user = User(username=data["username"], password=hashed_password)
    user.save()
    return {"message": "User registered successfully"}

def login_user(data):
    user = User.query.filter_by(username=data["username"]).first()
    if not user or not check_password_hash(user.password, data["password"]):
        return {"error": "Invalid credentials"}
    return {"message": "Login successful"}
