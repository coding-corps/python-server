from flask import Blueprint
from app.controllers.recipe_controller import daily_recipe, search

recipe_bp = Blueprint("recipe", __name__)
recipe_bp.route("/daily", methods=["GET"])(daily_recipe)
recipe_bp.route("/search", methods=["GET"])(search)
