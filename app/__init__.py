from flask import Flask
from app.config.settings import Config
from app.extensions import db, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    jwt.init_app(app)

    from app.routes import register_routes
    register_routes(app)

    return app
