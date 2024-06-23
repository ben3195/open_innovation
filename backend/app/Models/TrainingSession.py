from app import db, ma

class TrainingSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    athlete_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    sports = db.relationship('Sport', backref='training_session', lazy=True)

    def __init__(self, trainer_id, athlete_id, title, description, date, sports):
        self.trainer_id = trainer_id
        self.athlete_id = athlete_id
        self.title = title
        self.description = description
        self.date = date
        self.sports = sports

class TrainingSessionSchema(ma.Schema):
    class Meta:
        model = TrainingSession
        include_relationships = True
        load_instance = True

training_session_schema = TrainingSessionSchema(many=True)
