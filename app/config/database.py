from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .settings import settings  # Import settings object


# Construct the DATABASE_URL dynamically using the settings object
DATABASE_URL = settings.get_db_url()

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Create a base class for models
Base = declarative_base()

def get_db():
    """
    Dependency to get a database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """
    Initializes the database by creating tables based on the models.
    This function will create all tables that have been defined using the Base class.
    """
    # Import all models here to ensure they are registered with the metadata

    # Create all tables based on the Base metadata
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")
