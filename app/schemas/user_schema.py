# Pydantic models
from pydantic import BaseModel,  EmailStr  

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

    
class UserCreateSchema(BaseModel):
    username: str  
    password: str 
    email: str 


class UserUpdatePasswordSchema(BaseModel):
    current_password: str 
    new_password: str  
