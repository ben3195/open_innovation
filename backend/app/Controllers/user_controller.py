from flask import jsonify, request
from app import db
from app.Models.User import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

def user_login():
    email = request.json.get('email', None)
    password = request.json.get(check_password_hash('password', None))

    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Bad username or password"}), 401


def get_users():
    all_users = User.query.all()
    user_list = []
    for user in all_users:
        user_data = {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'birthdate': user.birth_date,
            'is_trainer': user.is_trainer
        }
        user_list.append(user_data)
    return jsonify(users=user_list)

def get_user(user_id):
    user = User.query.get(user_id)
    user_data = {
        'id': user.id,
        'email': user.email,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'birthdate': user.birth_date,
        'is_trainer': user.is_trainer
    }
    return jsonify(user_data)

def add_user():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    birth_date = data.get('birth_date')
    password = generate_password_hash(data.get('password'))
    is_trainer = data.get('is_trainer', False)

    new_user = User(email=email, username=username, first_name=first_name, last_name=last_name, password=password, birth_date=birth_date, is_trainer=is_trainer)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully.'})

def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.get_json()
    user.email = data.get('email', user.email)
    user.username = data.get('username', user.username)
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.birth_date = data.get('birth_date', user.birth_date)
    if 'password' in data:
        user.password = generate_password_hash(data.get('password'))
    user.is_trainer = data.get('is_trainer', user.is_trainer)

    db.session.commit()

    return jsonify({'message': 'User updated successfully.'})

def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully.'})
