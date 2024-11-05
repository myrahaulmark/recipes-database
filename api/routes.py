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
# Categories
# ---------------------------------------------------------
# GET route to fetch all recipe categories with no limit
@api_bp.route("/categories", methods=["GET"])
def get_categories_endpoint():
    """
    Retrieve all recipe categories.
    
    Returns:
        tuple: JSON response containing categories and HTTP status code 200.
    """
    categories = services.get_categories()  # Call the service function to get categories
    return jsonify(categories), 200


# GET route to fetch all users with no limit
@api_bp.route("/users", methods=["GET"])
def get_users_endpoint():
    """
    Retrieve all users.
    
    Returns:
        tuple: JSON response containing users and HTTP status code 200.
    """
    categories = services.get_all_users()  # Call the service function to get categories
    return jsonify(categories), 200


#STILL EDITING
@api_bp.route('/Reviews/<int:RecipeID>', methods=['GET'])
def get_reviews_for_recipe(RecipeID):
    """
    Retrieve Review information for a specific RecipeID.

    Args:
        RecipeID (int): The unique identifier of the recipe.

    Returns:
        tuple: A tuple containing a JSON response and an HTTP status code.
            - If the user is found, returns a JSON object with user information and status code 200.
            - If the user is not found, returns a JSON object with an error message and status code 404.
    """
    
    # Example: /api/users/1
    
    # Using the database services to get the user by ID
    reviews = services.get_reviews_for_recipe(RecipeID)
    if reviews:
        return jsonify([dict(review) for review in reviews]), 200
    return jsonify({'message': 'No reviews found'}), 404
 

# ---------------------------------------------------------
# Recipes
# ---------------------------------------------------------

# ---------------------------------------------------------
# Ingredients
# ---------------------------------------------------------

# ---------------------------------------------------------
# Reviews
# ---------------------------------------------------------

# ---------------------------------------------------------
# Instructions
# ---------------------------------------------------------

# ---------------------------------------------------------
# Users
# ---------------------------------------------------------