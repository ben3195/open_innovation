# backend/app/Models/SessionSports.py

from app import db, ma

class SessionSports(db.Model):
    __tablename__ = 'session_sports'
    id = db.Column(db.Integer, primary_key=True)
    training_session_id = db.Column(db.Integer, db.ForeignKey('training_session.id'), nullable=False)
    sport_id = db.Column(db.Integer, db.ForeignKey('sport.id'), nullable=False)

    def __init__(self, training_session_id, sport_id):
        self.training_session_id = training_session_id
        self.sport_id = sport_id

class SessionSportsSchema(ma.Schema):
    class Meta:
        model = SessionSports
