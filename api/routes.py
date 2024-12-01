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
    categories = services.get_categories()
    return jsonify(categories), 200

# GET route to fetch all appetizers at random
@api_bp.route('/recipes/appetizers/random', methods=['GET'])
def get_random_appetizer_recipes_route():
    """
    API endpoint to fetch up to 6 random appetizer recipes.
    """
    try:
        recipes = services.get_random_appetizer_recipes(limit=6)  # Pass the limit argument here
        if not recipes:
            return jsonify({"error": "No recipes found in Appetizers category"}), 404
        return jsonify({"recipes": recipes}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET route to fetch all soups at random
@api_bp.route('/recipes/soups/random', methods=['GET'])
def get_random_soup_recipes_route():
    """
    API endpoint to fetch up to 6 random soup recipes.
    """
    try:
        recipes = services.get_random_soup_recipes(limit=6)  # Pass the limit argument here
        if not recipes:
            return jsonify({"error": "No recipes found in Soups category"}), 404
        return jsonify({"recipes": recipes}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET route to fetch all desserts at random
@api_bp.route('/recipes/desserts/random', methods=['GET'])
def get_random_desserts_recipes_route():
    """
    API endpoint to fetch up to 6 random soup recipes.
    """
    try:
        recipes = services.get_random_dessert_recipes(limit=6)  # Pass the limit argument here
        if not recipes:
            return jsonify({"error": "No recipes found in Soups category"}), 404
        return jsonify({"recipes": recipes}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------
# Users
# ---------------------------------------------------------
# GET route to fetch all users with no limit
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

# Add a user
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

# Delete a user
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

# Update a user
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
@api_bp.route('/Reviews/<int:RecipeID>', methods=['GET'])
def get_reviews_for_recipe(RecipeID):
    """
    Retrieve review information for a specific RecipeID.

    Args:
        RecipeID (int): The unique identifier of the recipe.

    Returns:
        tuple: A tuple containing a JSON response and an HTTP status code.
            - If the user is found, returns a JSON object with user information and status code 200.
            - If the user is not found, returns a JSON object with an error message and status code 404.
    """
    reviews = services.get_reviews_for_recipe(RecipeID)
    if reviews:
        return jsonify([dict(review) for review in reviews]), 200
    return jsonify({'message': 'No reviews found'}), 404

# ---------------------------------------------------------
# Recipes
# ---------------------------------------------------------
@api_bp.route('/recipes/limited', methods=['GET'])
def get_limited_recipes_endpoint():
    """
    Retrieve a limited number of recipes.

    Args:
        limit (int, optional): The maximum number of recipes to retrieve. Default is 10.

    Returns:
        tuple: JSON response containing recipes and HTTP status code 200.
    """
    limit = request.args.get('limit', default=10, type=int)
    recipes = services.get_limited_recipes(limit)
    if recipes:
        return jsonify([dict(recipe) for recipe in recipes]), 200
    return jsonify({'message': 'No recipes found'}), 404

# Get the recipe and alll details
@api_bp.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_appetizer_recipe(recipe_id):
    try:
        recipe = services.fetch_recipe(recipe_id)
        if not recipe:
            return jsonify({"error": "Recipe not found"}), 404
        return jsonify(recipe), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Getting an appetizer recipe by keyword search in title
@api_bp.route('/recipes/appetizers/search', methods=['GET'])
def search_appetizers_route():
    """
    API endpoint to search for appetizers by keyword in the title.
    """
    try:
        # Retrieve the keyword from the query string
        keyword = request.args.get('q')
        if not keyword:
            return jsonify({"error": "Keyword is required"}), 400

        # Call the search function
        results = services.search_appetizers_by_title(keyword)
        if not results:  # If no results are found
            return jsonify({"message": "No matching appetizers found"}), 404

        # Return the results in JSON format
        return jsonify({"recipes": results}), 200

    except Exception as e:
        # Handle unexpected errors and return an error message
        return jsonify({"error": str(e)}), 500

# Getting a soup recipe by keyword search in title
@api_bp.route('/recipes/soups/search', methods=['GET'])
def search_soups_route():
    """
    API endpoint to search for soups by keyword in the title.
    """
    try:
        # Retrieve the keyword from the query string
        keyword = request.args.get('q')
        if not keyword:
            return jsonify({"error": "Keyword is required"}), 400

        # Call the search function
        results = services.search_soups_by_title(keyword)
        if not results:  # If no results are found
            return jsonify({"message": "No matching soup recipes found"}), 404

        # Return the results in JSON format
        return jsonify({"recipes": results}), 200

    except Exception as e:
        # Handle unexpected errors and return an error message
        return jsonify({"error": str(e)}), 500

# Getting a dessert recipe by keyword search in title
@api_bp.route('/recipes/desserts/search', methods=['GET'])
def search_desserts_route():
    """
    API endpoint to search for desserts by keyword in the title.
    """
    try:
        # Retrieve the keyword from the query string
        keyword = request.args.get('q')
        if not keyword:
            return jsonify({"error": "Keyword is required"}), 400

        # Call the search function
        results = services.search_desserts_by_title(keyword)
        if not results:  # If no results are found
            return jsonify({"message": "No matching dessert recipes found"}), 404

        # Return the results in JSON format
        return jsonify({"recipes": results}), 200

    except Exception as e:
        # Handle unexpected errors and return an error message
        return jsonify({"error": str(e)}), 500

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


 # searching for recipes with a group of keywords
@api_bp.route('/recipes/search-by-ingredients', methods=['GET'])
def search_recipes_by_ingredients_route():
    """
    API endpoint to search for recipes by ingredients with partial matches.
    """
    try:
        ingredients = request.args.getlist('ingredients')  # Get the list of ingredients
        if not ingredients or len(ingredients) < 2:
            return jsonify({"error": "Please provide at least 2 ingredients."}), 400

        # Allow recipes that match at least 2 of the provided ingredients
        min_matches = max(len(ingredients) - 1, 2)

        results = services.search_recipes_by_ingredients(ingredients, min_matches=min_matches)
        if not results:
            return jsonify({"message": "No matching recipes found."}), 404

        return jsonify({"recipes": results}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500




# ---------------------------------------------------------
# Instructions
# ---------------------------------------------------------\
@api_bp.route('/instructions/<recipe_title>', methods=['GET']) 
def get_instructions_by_recipe_title(recipe_title): 
    instructions = services.get_instructions_by_recipe_title(recipe_title) 
    if instructions: 
        return jsonify(instructions), 200 
    else: 
        return jsonify({"message": "No instructions found for this recipe"}), 404
    

# ---------------------------------------------------------
# ADDING A RECIPE FOR FRONTEND APP
# ---------------------------------------------------------
from flask import request, jsonify
from api.services import add_recipe_with_details

@api_bp.route('/recipes/add', methods=['POST'])
def add_recipe_route():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input, JSON data required"}), 400

        # Add recipe with details
        recipe_id = services.add_recipe_with_details(
            title=data["Title"],
            description=data.get("Description", ""),
            cooking_time=data["CookingTime"],
            servings=data["Servings"],
            ingredients=data["Ingredients"],
            instructions=data["Instructions"]
        )
        return jsonify({"message": "Recipe added successfully", "RecipeID": recipe_id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

