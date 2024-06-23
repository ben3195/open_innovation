# backend/app/Models/User.py

from app import db, ma
from .TrainingSession import TrainingSession  # Assurez-vous que l'import est correct

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.DateTime)
    is_trainer = db.Column(db.Boolean, default=False)

    athlete_sessions = db.relationship('TrainingSession', foreign_keys='TrainingSession.athlete_id', backref='athlete', lazy=True)
    trainer_sessions = db.relationship('TrainingSession', foreign_keys='TrainingSession.trainer_id', backref='trainer', lazy=True)

    def __init__(self, email, username, first_name, last_name, password, birth_date, is_trainer=False):
        self.email = email
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.birth_date = birth_date
        self.is_trainer = is_trainer

class UserSchema(ma.Schema):
    class Meta:
        model = User
        load_only = 'password'
        dump_only = 'id'
