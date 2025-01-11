from flask import request, jsonify
from app.services.recipe_service import get_daily_recipe, search_recipes

def daily_recipe():
    user_id = request.headers.get("user_id")
    result = get_daily_recipe(user_id)
    return jsonify(result)

def search():
    query = request.args.get("q")
    result = search_recipes(query)
    return jsonify(result)
