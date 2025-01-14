from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from passlib.context import CryptContext  # To hash passwords
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):  # Assuming Base is already declared
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)  # Is the user active?
    is_deleted = Column(Boolean, default=False, nullable=False)  # For soft delete functionality
    created_at = Column(DateTime, default=func.now())  # Timestamp for creation
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # Timestamp for last update
    last_login_at = Column(DateTime, nullable=True)  # Timestamp for the last login

    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    role = relationship("Role", back_populates="users")

    def set_password(self, password: str):
        self.hashed_password = pwd_context.hash(password)  # Hash the password before storing

    def check_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.hashed_password)  # Verify the hashed password

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}, is_active={self.is_active})>"




class Role(Base):  # Assuming Base is already declared
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)  # Role name (e.g., 'Admin', 'User')
    description = Column(String, nullable=True)  # Optional description for the role
    created_at = Column(DateTime, default=func.now())  # Timestamp for role creation
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # Timestamp for role updates

    def __repr__(self):
        return f"<Role(id={self.id}, name={self.name})>"


