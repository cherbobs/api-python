from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

api_bp = Blueprint('api', __name__)

@api_bp.route('/user', methods=['GET'])
@jwt_required()
def get_user():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
