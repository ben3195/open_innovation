from app import app
from app.Controllers.sport_controller import get_sport, get_sports

@app.route('/sports', methods=['GET'])
def all_sports_route():
    return get_sports()

@app.route('/sport/<int:sport_id>')
def sport_route(sport_id):
    return get_sport(sport_id)
