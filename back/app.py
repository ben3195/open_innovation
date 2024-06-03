from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/triathlon_app"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    username = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    birth_date = db.Column(db.DateTime, default=datetime.datetime.now)
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

user_schema = UserSchema()

@app.route('/')
def home():
    return "Welcome to TriathlonMinder!"

@app.route('/users', methods=['GET'])
def get_users():
    all_users = db.session.query(User).all()
    user_list = []
    for user in all_users:
        user = {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'password': user.password,
            'birthdate': user.birth_date,
            'is_trainer': user.is_trainer
        }
        user_list.append(user)

    return jsonify(users=user_list)

@app.route('/add/user', methods=['POST'])
def add_user():
    email = request.json['email']
    username = request.json['username']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    birth_date = request.json['birth_date']
    password = generate_password_hash(request.json['password'])
    is_trainer = request.json.get('isTrainer', False)

    new_user = User(email, username, first_name, last_name, password, birth_date, is_trainer)
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

if __name__ == '__main__':
    app.run(debug=True)
