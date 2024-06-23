from app import db

class SessionSports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    training_session_id = db.Column(db.Integer, db.ForeignKey('training_session.id'), nullable=False)
    sport_id = db.Column(db.Integer, db.ForeignKey('sport.id'), nullable=False)
