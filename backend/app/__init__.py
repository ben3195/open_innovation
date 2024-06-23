from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

# Initialisation de l'application Flask
app = Flask(__name__)

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/triathlon_app"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
JWT_SECRET_KEY = 'my_key'

# Initialisation de SQLAlchemy
db = SQLAlchemy(app)

# Initialisation de Marshmallow
ma = Marshmallow(app)

# Initialisation de JWT
jwt = JWTManager(app)

# Importer les vues et les modèles après l'initialisation de db et ma
from app.Models import User, Sport, TrainingSession, SessionSports
from app.Views import user_view
from app.Views import sport_view
from app.Views import training_session_view
