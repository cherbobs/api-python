# api-python

## Description
Cette API Flask permet de gérer des utilisateurs, y compris l'enregistrement, la connexion et la mise à jour des informations utilisateur.

### Fonctionnalités :
- Enregistrement d'un utilisateur : Crée un nouvel utilisateur avec un nom d'utilisateur, un email et un mot de passe.
- Connexion : Génère un token JWT pour les utilisateurs qui se connectent avec succès.
- Mise à jour des informations utilisateur : Permet de mettre à jour les informations d'un utilisateur existant (nom d'utilisateur, email, mot de passe).

---

 Prérequis
Avant de commencer, assurez-vous d'avoir installé les éléments suivants sur votre machine :
- Python 3.x
- Flask
- Flask-JWT-Extended
- Flask-Migrate
- Une base de données MySQL ou PostgreSQL (gérée via SQLAlchemy)

---

 Installation

1. Clonez le projet sur votre machine locale :
   ```bash
   git clone https://github.com/votre-repo/api-python.git
   cd api-python

2. Créez et activez un environnement virtuel :

bash
Copier le code
python3 -m venv env
source env/bin/activate  # Sous Windows : env\Scripts\activate

3. Installez les dépendances requises :

bash
Copier le code
pip install -r requirements.txt

4. Configurez la base de données :

Modifiez les informations de connexion à la base de données dans le fichier config.py.
Initialisez la base de données :
bash
Copier le code
flask db init
flask db migrate
flask db upgrade

5. Configurez les variables d'environnement dans .env et démarrez le serveur Flask
flask run

7. Endpoints

Inscription d'un utilisateur :
URL : /auth/register
Méthode : POST
Données d'entrée :
  {
  "username": "nom_utilisateur",
  "email": "email",
  "password": "mot_de_passe"
  }


Connexion d'un utilisateur :
URL : /auth/login
Méthode : POST
Données d'entrée :
  {
  "username": "nom_utilisateur",
  "password": "mot_de_passe"
  }

Mise à jour des informations d'un utilisateur :
URL : /users/<user_id>
Méthode : PUT
Headers : Authorization: Bearer <mon_token>

Données d'entrée pour tester :
{
  "username": "nv_nom_utilisateur",
  "email": "nv_email",
  "password": "nv_mot_de_passe"
}


Tests
Vous pouvez utiliser Postman ou un autre outil similaire pour envoyer des requêtes HTTP pour tester.
