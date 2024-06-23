from app import app
from app.Controllers.training_session_controller import get_all_training_sessions, get_training_session, add_training_session, update_training_session, delete_training_session
from flask_jwt_extended import jwt_required


@app.route('/training_sessions', methods=['GET'])
@jwt_required()
def all_training_session():
    return get_all_training_sessions()

@app.route('/training_session/<int:training_session_id>', methods=['GET'])
def get_training_session_route(training_session_id):
    return get_training_session(training_session_id)

@app.route('/add/training_session', methods=['POST'])
def add_training_session_route():
    return add_training_session()

@app.route('/update/user/<int:user_id>', methods=['PUT'])
def update_training_session_route(training_session_id):
    return update_training_session(training_session_id)

@app.route('/delete/training_session/<int:training_session_id>', methods=['DELETE'])
def delete_training_session_route(training_session_id):
    return delete_training_session(training_session_id)
