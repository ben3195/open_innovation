from flask import jsonify
from app.Models.Sport import Sport

def get_sports():
    all_sports = Sport.query.all()
    sport_list = []
    for sport in all_sports:
        sport_data = {
            'id': sport.id,
            'name': sport.name
        }
        sport_list.append(sport_data)
    return jsonify(sports=sport_list)

def get_sport(sport_id):
    sport = Sport.query.get(sport_id)
    sport_data = {
        'id': sport.id,
        'name': sport.name
    }
    return jsonify(sport_data)
