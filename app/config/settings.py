from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

class Settings:
    app_name: str = "Cooking Compass"
    debug: bool = True
    secret_key: str = os.getenv("SECRET_KEY", "your_secret_key")
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "your_jwt_secret_key")
    algorithm: str = os.getenv("ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    # MySQL settings
    mysql_host: str = os.getenv("MYSQL_HOST")
    mysql_user: str = os.getenv("MYSQL_USER")
    mysql_password: str = os.getenv("MYSQL_PASSWORD")
    mysql_database: str = os.getenv("MYSQL_DB")
    mysql_port: str = os.getenv("MYSQL_PORT")

    class Config:
        env_file = ".env"

    def get_db_url(self):
        DATABASE_URL = f"mysql+pymysql://{self.mysql_user}:{self.mysql_password}@{self.mysql_host}:{self.mysql_port}/{self.mysql_database}"
        return DATABASE_URL

# Instantiate settings object 
settings = Settings()
