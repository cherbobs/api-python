from flask import Flask, render_template
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager

# Initialisation de PyMongo
mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    
    # Configuration MongoDB
    app.config["MONGO_URI"] = "mongodb+srv://Ismael:y3HqPgjjmLnTaKdT@clusterlocal.unengax.mongodb.net/?retryWrites=true&w=majority&appName=ClusterLocal"

    # Initialisation de PyMongo avec l'application Flask
    mongo.init_app(app)

    # Initialisation de JWTManager
    JWTManager(app)

    # Importation des blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Page d'accueil
    @app.route('/')
    def home():
        return render_template('index.html')

    return app
