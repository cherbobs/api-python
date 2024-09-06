from flask import Flask, jsonify, request, abort
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Configuration de la connexion à MongoDB (ici un exemple avec une base de données locale)
app.config["MONGO_URI"] = "mongodb+srv://Ismael:y3HqPgjjmLnTaKdT@clusterlocal.unengax.mongodb.net/?retryWrites=true&w=majority&appName=ClusterLocal"
mongo = PyMongo(app)

# Collection d'utilisateurs
users_collection = mongo.db

@app.route('/delete_user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        # Convertir l'ID en ObjectId pour MongoDB
        result = users_collection.delete_one({"_id": ObjectId(user_id)})
        
        if result.deleted_count == 1:
            return jsonify({"message": f"User with id {user_id} has been deleted"}), 200
        else:
            return jsonify({"error": "User not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
