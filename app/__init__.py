from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .models import db  # Assure-toi que db est bien importé depuis models
from .auth import auth_bp
from .routes import api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    JWTManager(app)

    # Initialisation de Flask-Migrate
    migrate = Migrate(app, db)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
