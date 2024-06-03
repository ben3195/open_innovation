from app import db, ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    username = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    birth_date = db.Column(db.DateTime)
    is_trainer = db.Column(db.Boolean, default=False)

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
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password', 'birth_date', 'is_trainer')
        load_only = 'password'
        dump_only = 'id'