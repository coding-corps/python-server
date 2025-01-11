from flask import request, jsonify
from app.services.profile_service import update_points, get_profile

def get_user_profile():
    user_id = request.headers.get("user_id")
    result = get_profile(user_id)
    return jsonify(result)

def add_points():
    data = request.json
    result = update_points(data["user_id"], data["points"])
    return jsonify(result)
