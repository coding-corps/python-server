from app.models.user_model import User
from app.schemas.auth_schema import AuthSchema
# from app.config.database import SessionLocal

class AuthService:
    
    @staticmethod
    def login(auth: AuthSchema):
        # db = SessionLocal()
        # user = db.query(User).filter(User.username == auth.username).first()
        # if user and user.password == auth.password:
        #     return user
        return None

    @staticmethod
    def register(auth: AuthSchema):
        # db = SessionLocal()
        # new_user = User(username=auth.username, password=auth.password)
        # db.add(new_user)
        # db.commit()
        # db.refresh(new_user)
        return None
