from fastapi import FastAPI
from app.routes import user_routes, auth_routes
from app.controllers.healthcheck import healthcheck
from app.config.database import init_db
# from app.middlewares.auth_middleware import AuthMiddleware
# from app.utils.logger import setup_logging
from app.config.settings import Settings

 
# Initialize the app
app = FastAPI()


# Setup logging
# setup_logging()

# Include routers
app.include_router(auth_routes, prefix="/auth", tags=["Authentication"])
app.include_router(user_routes, prefix="/users", tags=["Users"])

app.add_api_route("/health", healthcheck, methods=["GET"],tags=["Health"] )

# Initialize database
@app.on_event("startup")
def on_startup():
    print("starting up")
    init_db()

# Add middleware
# app.add_middleware(AuthMiddleware)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to Cooking Compass!"}
