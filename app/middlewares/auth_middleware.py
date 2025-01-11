from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request

def auth_required(func):
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
        except:
            return jsonify({"error": "Unauthorized"}), 401
        return func(*args, **kwargs)
    return wrapper
