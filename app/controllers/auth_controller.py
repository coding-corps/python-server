from flask import request, jsonify
from app.services.auth_service import register_user, login_user

def register():
    data = request.json
    result = register_user(data)
    return jsonify(result)

def login():
    data = request.json
    result = login_user(data)
    return jsonify(result)
