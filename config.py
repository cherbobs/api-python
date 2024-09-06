import os

class Config:
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')  # Change 'my_secret_key' par une valeur plus sécurisée
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'my_jwt_secret')  # Change 'my_jwt_secret' par une valeur plus sécurisée
    MONGO_URI = "mongodb+srv://Ismael:y3HqPgjjmLnTaKdT@clusterlocal.unengax.mongodb.net/?retryWrites=true&w=majority&appName=ClusterLocal"

