from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import User, db

user_management_bp = Blueprint('user_management', __name__)

@user_management_bp.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    # Obtenir l'ID de l'utilisateur actuel à partir du token JWT
    current_user = get_jwt_identity()
    current_user_id = current_user['user_id']

    # Vérifier que l'ID utilisateur correspond à celui du token JWT
    if user_id != current_user_id:
        return jsonify({'message': 'Permission denied'}), 403

    # Récupérer l'utilisateur à mettre à jour
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Mettre à jour les informations de l'utilisateur
    data = request.get_json()
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    if 'password' in data:
        user.password = generate_password_hash(data['password'])

    # Sauvegarder les modifications dans la base de données
    db.session.commit()

    # Répondre avec les nouvelles informations de l'utilisateur
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
    }), 200
