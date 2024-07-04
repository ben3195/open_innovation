from flask import jsonify, request
from app import db
from app.Models.TrainingSession import TrainingSession, TrainingSessionSchema
from app.Models.SessionSports import SessionSports, SessionSportsSchema
from app.Models.User import User
from flask_jwt_extended import get_jwt_identity

training_session_schema = TrainingSessionSchema()

def get_all_training_sessions():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if user.is_trainer:
        sessions = TrainingSession.query.filter_by(trainer_id=current_user_id).all()
    else:
        sessions = TrainingSession.query.filter_by(athlete_id=current_user_id).all()

    return training_session_schema.jsonify(sessions)

def get_training_session(training_session_id):
    training_session = TrainingSession.query.get(training_session_id)
    print(type(training_session))
    if not training_session:
        return jsonify({'message': 'Training session not found'}), 404

    result = training_session_schema.dump(training_session)
    return jsonify(result)

def add_training_session():
    data = request.get_json()

    # Récupérer les informations pour TrainingSession
    trainer_id = data.get('trainer_id')
    athlete_id = data.get('athlete_id')
    title = data.get('title')
    description = data.get('description')
    date = data.get('date')

    # Récupérer les informations pour SessionSports
    sports = data.get('sports', [])  # Liste des sports, peut en contenir plusieurs

    new_training_session = TrainingSession(trainer_id=trainer_id, athlete_id=athlete_id, title=title, description=description, date=date)

    db.session.add(new_training_session)
    db.session.commit()

    for sport_id in sports:
        new_session_sport = SessionSports(training_session_id=new_training_session.id, sport_id=sport_id)
        db.session.add(new_session_sport)

    db.session.commit()

    return jsonify({'message': 'Training session added successfully.'})


def update_training_session(training_session_id):
    training_session = TrainingSession.query.get(training_session_id)
    if not training_session:
        return jsonify({'message': 'Training session not found'}), 404

    data = request.get_json()
    training_session.trainer_id = data.get('trainer_id', training_session.trainer_id)
    training_session.athlete_id = data.get('athlete_id', training_session.athlete_id)
    training_session.title = data.get('title', training_session.title)
    training_session.description = data.get('description', training_session.description)
    training_session.date = data.get('date', training_session.date)
    training_session.sports = data.get('sports', training_session.sports)

    db.session.commit()

    return jsonify({'message': 'Training session updated successfully.'})


def delete_training_session(training_session_id):
    training_session = TrainingSession.query.get(training_session_id)
    db.session.delete(training_session)
    db.session.commit()
    return jsonify({'message': 'Training session deleted successfully.'})
