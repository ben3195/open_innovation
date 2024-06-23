from app import db, ma

class Sport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, email, username, first_name, last_name, password, birth_date, is_trainer=False):
        self.email = email
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.birth_date = birth_date
        self.is_trainer = is_trainer

class SportSchema(ma.Schema):
    class Meta:
        model = Sport
        dump_only = 'id'
