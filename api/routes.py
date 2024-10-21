from flask import jsonify, request, Blueprint
import api.services as services
from api.models import User, Category, Recipe, Ingredient, RecipeCategoryFact, RecipeIngredientsFact, Review, Instruction

# Create a Blueprint instance
# This will allow us to group related routes together. All the routes in this file will be part of the 'api' Blueprint.
# This means that the routes will be accessible at '/api/' followed by the route path.
# For instance, the route '/users' will be accessible at '/api/users'.
# We can then register the Blueprint with the Flask app in the main.py file.

api_bp = Blueprint("api", __name__)

@api_bp.route('/')
def home():
    return 'Welcome to the User API!', 200

@api_bp.route('/connection')
def test_connection():
    """
    Test the database connection.

    Returns:
        tuple: A tuple containing a JSON response with a message and an HTTP status code.
    """
    services.get_db_connection()
    return jsonify({'message': 'Successfully connected to the API'}), 200
    return "Connection successful!"

# ---------------------------------------------------------
# Users
# ---------------------------------------------------------

# ---------------------------------------------------------
# Categories
# ---------------------------------------------------------

# ---------------------------------------------------------
# Recipes
# ---------------------------------------------------------
# GET route to fetch all recipes with a limit
@api_bp.route('/recipes', methods=['GET'])  # Corrected


def get_recipes():
    limit = request.args.get('limit', default=10, type=int)
    return jsonify(recipes[:limit])


# ---------------------------------------------------------
# Ingredients
# ---------------------------------------------------------

# ---------------------------------------------------------
# Reviews
# ---------------------------------------------------------

# ---------------------------------------------------------
# Instructions
# ---------------------------------------------------------