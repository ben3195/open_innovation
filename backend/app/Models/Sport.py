from app import db, ma

class Sport(db.Model):
    __tablename__ = 'sport'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

class SportSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sport
        load_instance = True

sport_schema = SportSchema()
sports_schema = SportSchema(many=True)