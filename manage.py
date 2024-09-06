from app import create_app
from app.models import db
from flask_migrate import Migrate
from app.user_management import user_management_bp
from app.auth import auth_bp  # Assure-toi d'importer le blueprint auth

app = create_app()
migrate = Migrate(app, db)

# Enregistrement des blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_management_bp, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True)
