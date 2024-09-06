from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from .models import User, db
from flask import Flask, redirect, url_for
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'])
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    access_token = create_access_token(identity={'username': user.username})
    return jsonify(access_token=access_token), 200

app = Flask(__name__)

# Configuration de l'application Flask (par exemple, connexion à la base de données)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Exemple avec SQLite
db.init_app(app)

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    # Rechercher l'utilisateur dans la base de données
    user = User.query.get(user_id)
    
    if user:
        # Si l'utilisateur existe, on le supprime
        db.session.delete(user)
        db.session.commit()
        return f"L'utilisateur avec l'id {user_id} a été supprimé."
    else:
        return f"L'utilisateur avec l'id {user_id} n'existe pas."

if __name__ == '__main__':
    app.run(debug=True)
