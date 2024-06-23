from app import app
from app.Controllers.user_controller import user_login, get_users, add_user, get_user, update_user, delete_user

@app.route('/')
def index():
    return "Hello World!"

@app.route('/login', methods=['POST'])
def login_route():
    return user_login()

@app.route('/users', methods=['GET'])
def users():
    return get_users()

@app.route('/user/<int:user_id>')
def user_route(user_id):
    return get_user(user_id)

@app.route('/add/user', methods=['POST'])
def add_user_route():
    return add_user()

@app.route('/update/user/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    return update_user(user_id)

@app.route('/delete/user/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    return delete_user(user_id)
