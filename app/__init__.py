from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import jwt_manager,create_access_token
from app.routes import auth
from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = jwt_manager.JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    app.register_blueprint(auth.auth)

    return app