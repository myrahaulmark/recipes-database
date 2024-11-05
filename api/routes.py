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

# ---------------------------------------------------------
# Users
# ---------------------------------------------------------

# GET route to fetch all users with no limit
from flask import jsonify, request, Blueprint
import api.services as services

api_bp = Blueprint("api", __name__)

@api_bp.route("/users", methods=["GET"])
def get_users_endpoint():
    """
    Retrieve a list of users filtered by last name.
    If the query parameter 'name' is provided, filter users by last names that start with the provided string.
    If 'starts_with' is False, filter users by last names that contain the provided string.

    Query Parameters:
        name (str): The string to filter last names by.
        starts_with (bool, optional): If True, filter names that start with the string. Defaults to True.

    Returns:
        JSON response with a list of users.
    """
    name = request.args.get("name")
    starts_with = request.args.get("starts_with", "true").lower() == "true"

    # Validate 'name' parameter
    if not name:
        return jsonify({"error": "The 'name' query parameter is required."}), 400

    # Call the function to get filtered users
    users = services.get_users_by_name(name, starts_with=starts_with)
    return jsonify(users), 200

#Add a user
@api_bp.route('/users', methods=['POST'])
def add_user():
    """
    Add a new user to the database.
    Expects JSON payload with 'FirstName', 'LastName', 'Email', and 'JoinDate'.
    """
    data = request.get_json()

    # Ensure all required fields are present
    if not all(field in data for field in ['FirstName', 'LastName', 'Email', 'JoinDate']):
        return jsonify({"error": "Missing required fields"}), 400

    # Add the user to the database using the service function
    user_id = services.add_user(
        first_name=data['FirstName'],
        last_name=data['LastName'],
        email=data['Email'],
        join_date=data['JoinDate']
    )
    return jsonify({"message": "User added successfully", "UserID": user_id}), 201

#Delete a user
@api_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user by UserID.
    """
    success = services.delete_user(user_id)
    if success:
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

#update a user
@api_bp.route('/users/<int:UserID>', methods=['PUT'])
def update_user(UserID):
    data = request.get_json()
    
    # Validate input
    if not data or 'FirstName' not in data or 'LastName' not in data or 'Email' not in data:
        return jsonify({"error": "Fields 'FirstName', 'LastName', and 'Email' are required"}), 400
    
    # Call the services function to update user details
    success = services.update_user_by_id(UserID, data['FirstName'], data['LastName'], data['Email'])
    
    if success:
        return jsonify({"message": "User updated successfully"}), 200
    else:
        return jsonify({"error": "User not found"}), 404




# ---------------------------------------------------------
# Reviews
# ---------------------------------------------------------
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
@api_bp.route('/ingredients/<int:recipe_id>', methods=['GET'])
def get_ingredients_for_recipe(recipe_id):
    ingredients = services.get_ingredients_with_amounts_by_recipe_id(recipe_id)
    if ingredients:
        return jsonify(ingredients), 200
    else:
        return jsonify({"message": "No ingredients found for this recipe"}), 404




# ---------------------------------------------------------
# Instructions
# ---------------------------------------------------------

