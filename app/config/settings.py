from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

class Settings:
    app_name: str = "Cooking Compass"
    debug: bool = True
    database_url: str = os.getenv("DATABASE_URL", "mysql+pymysql://root:password@db:3306/cooking_compass")
    secret_key: str = os.getenv("SECRET_KEY", "your_secret_key")
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "jwt_secret_key")
    algorithm: str = os.getenv("ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    # MySQL settings
    mysql_root_password: str = os.getenv("MYSQL_ROOT_PASSWORD", "password")
    mysql_database: str = os.getenv("MYSQL_DATABASE", "cooking_compass")

    class Config:
        env_file = ".env"

# Instantiate settings object 
settings = Settings()

