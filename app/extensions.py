from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from fastapi_jwt_auth import AuthJWT

# Database configuration
DATABASE_URL = "sqlite+aiosqlite:///./test.db"  # Replace with your actual database URL

# Create SQLAlchemy engine and session factory
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency for database session
async def get_db():
    async with async_session() as session:
        yield session


class Settings():
    authjwt_secret_key: str = "your-secret-key"  # Replace with your actual secret key

 

@AuthJWT.load_config
def get_config():
    return Settings()
