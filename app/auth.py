from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

# Route d'inscription
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # Récupérer les données du corps de la requête
    mongo = current_app.extensions['pymongo']  # Accéder à l'instance MongoDB

    # Vérifier si le nom d'utilisateur ou l'email existe déjà
    existing_user = mongo.db.users.find_one({'username': data['username']})
    if existing_user:
        return jsonify({'error': 'Username already exists'}), 409

    existing_email = mongo.db.users.find_one({'email': data['email']})
    if existing_email:
        return jsonify({'error': 'Email already registered'}), 409

    # Insérer le nouvel utilisateur avec un mot de passe hashé
    hashed_password = generate_password_hash(data['password'])
    mongo.db.users.insert_one({
        'username': data['username'],
        'email': data['email'],
        'password': hashed_password
    })

    return jsonify({'message': 'User created successfully'}), 201

# Route de connexion
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    access_token = create_access_token(identity={'username': user.username})
    return jsonify(access_token=access_token), 200
