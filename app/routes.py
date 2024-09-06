from flask import Blueprint, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity

api_bp = Blueprint('api', __name__)

@api_bp.route('/user', methods=['GET'])
@jwt_required()  # Protéger cette route avec JWT
def get_user():
    mongo = current_app.extensions['pymongo']
    
    # Obtenir l'identité de l'utilisateur connecté à partir du token JWT
    current_user = get_jwt_identity()

    # Chercher l'utilisateur dans MongoDB
    user = mongo.db.users.find_one({'username': current_user})
    
    if user:
        return jsonify({
            'username': user['username'],
            'email': user['email']
        }), 200
    else:
        return jsonify({'error': 'User not found'}), 404
