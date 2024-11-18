from multiprocessing.resource_tracker import getfd
import sqlite3
from api.models import User, Category, Recipe, Ingredient, RecipeCategoryFact, RecipeIngredientsFact, Review, Instruction
from typing import List
from pathlib import Path

def get_db_connection():
    """
    Establishes and returns a connection to the SQLite database.

    The connection uses 'data/my_recipes.db' as the database file and sets the
    row factory to sqlite3.Row, allowing access to columns by name.

    Returns:
        sqlite3.Connection: A connection object to the SQLite database.
    """
    DATABASE_PATH = Path(__file__).parents[1] / "data"
    connection = sqlite3.connect(DATABASE_PATH/'my_recipes.db')
    connection.row_factory = sqlite3.Row  # This allows you to access columns by name
    return connection

# Get a limited number of recipes -10
def get_limited_recipes(limit=10):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Recipes LIMIT ?", (limit,))
    return cursor.fetchall()

# ---------------------------------------------------------
# Related to Categories
# ---------------------------------------------------------
# Get all categories
import sqlite3
from typing import List, Dict

def get_categories() -> List[Dict]:
    """
    Retrieves all categories from the database.

    Returns:
        List[Dict]: A list of dictionaries representing categories.
    """
    # Establish a database connection and set row_factory for dictionary-like rows
    connection = get_db_connection()
    connection.row_factory = sqlite3.Row  # Enables dictionary-style access
    cursor = connection.cursor()

    # Execute the query and fetch categories
    cursor.execute("SELECT CategoryID, CategoryName FROM Categories")
    categories = [dict(row) for row in cursor.fetchall()]  # Map each row to a dictionary

    # Close the connection
    connection.close()

    return categories

# Get recipes in Appetizers with ingredients, instructions and reviews
def get_random_appetizer_recipes(limit=6):
    """
    Fetches up to `limit` random recipes from the 'Appetizers' category.
    """
    query = """
        SELECT 
            r.RecipeID,
            r.Title AS RecipeName,
            r.Description,
            r.CookingTime,
            r.Servings,
            r.ImageURL
        FROM 
            Recipes r
        LEFT JOIN 
            Category_Recipe_fact_table rcft ON r.RecipeID = rcft.RecipeID
        LEFT JOIN 
            Categories c ON rcft.CategoryID = c.CategoryID
        WHERE 
            c.CategoryName = 'Appetizers'
        ORDER BY RANDOM()
        LIMIT ?;
    """
    connection = get_db_connection() 
    cursor = connection.cursor()
    cursor.execute(query, (limit,))
    rows = cursor.fetchall()
    connection.close()

    # Convert the rows into a structured JSON response
    recipes = []
    for row in rows:
        recipes.append({
            "RecipeID": row[0],
            "RecipeName": row[1],
            "Description": row[2],
            "CookingTime": row[3],
            "Servings": row[4],
            "ImageURL": row[5]
        })
    return recipes

    
# # Query the Review table for reviews matching the given RecipeID

def get_reviews_for_recipe(recipe_id: int):
    """
    Retrieves all reviews for a given recipe by RecipeID.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Fetch reviews for the given RecipeID
    cursor.execute("SELECT * FROM Reviews WHERE RecipeID = ?", (recipe_id,))
    reviews = cursor.fetchall()
    connection.close()
    
    return reviews

#Number of recipes available in each category
def get_recipe_count_by_category():
    """
    Retrieves the count of recipes in each category.
    """
    connection = get_db_connection()
    cursor = connection.cursor()

    # Execute the query to count recipes by category
    cursor.execute("""
        SELECT Categories.CategoryName, COUNT(Recipes.RecipeID) AS recipe_count
        FROM Recipes
        JOIN Category_Recipe_fact_table ON Recipes.RecipeID = Category_Recipe_fact_table.RecipeID
        JOIN Categories ON Category_Recipe_fact_table.CategoryID = Categories.CategoryID
        GROUP BY Categories.CategoryName;
    """)
    results = cursor.fetchall()
    connection.close()

    return results

# Get all users
def get_all_users():
    """
    Retrieve all users from the database.
    
    Returns:
        list: A list of dictionaries containing user data.
    """
    connection = get_db_connection()  # Use the connection function for consistency
    cursor = connection.cursor()
    
    # Adjusted to match the actual field names in your database
    cursor.execute("SELECT UserID, FirstName, LastName, Email, JoinDate FROM users")
    rows = cursor.fetchall()
    
    # Convert the data to a list of dictionaries
    user_list = [
        {
            "UserID": row["UserID"],
            "FirstName": row["FirstName"],
            "LastName": row["LastName"],
            "Email": row["Email"],
            "JoinDate": row["JoinDate"]
        }
        for row in rows
    ]
    
    connection.close()
    return user_list


def get_users_by_name(name, starts_with=True):
    """
    Retrieve users filtered by last name. Can either filter users by last names that
    start with the provided string or contain the provided string.

    Args:
        name (str): The string to filter last names by.
        starts_with (bool): If True, filter by last names that start with 'name'.
                            If False, filter by last names that contain 'name'.

    Returns:
        list: A list of dictionaries containing user data.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Update the query to filter by LastName
    if starts_with:
        query = "SELECT UserID, FirstName, LastName, Email FROM users WHERE LastName LIKE ?"
        cursor.execute(query, (f"{name}%",))
    else:
        query = "SELECT UserID, FirstName, LastName, Email FROM users WHERE LastName LIKE ?"
        cursor.execute(query, (f"%{name}%",))
    
    rows = cursor.fetchall()
    user_list = [
        {
            "UserID": row["UserID"], 
            "FirstName": row["FirstName"], 
            "LastName": row["LastName"], 
            "Email": row["Email"]
        } 
        for row in rows
    ]
    
    connection.close()
    return user_list

#add user 
def add_user(first_name, last_name, email, join_date):
    """
    Add a new user to the database.
    
    Args:
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        email (str): The user's email.
        join_date (str): The join date in 'YYYY-MM-DD' format.
    
    Returns:
        int: The ID of the newly added user.
    """
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO users (FirstName, LastName, Email, JoinDate) VALUES (?, ?, ?, ?)",
        (first_name, last_name, email, join_date)
    )
    connection.commit()
    user_id = cursor.lastrowid
    connection.close()
    return user_id

#delete user
def delete_user(user_id):
    """
    Delete a user from the database by UserID.
    
    Args:
        user_id (int): The unique ID of the user to delete.
    
    Returns:
        bool: True if the user was deleted, False if not found.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE UserID = ?", (user_id,))
    connection.commit()
    success = cursor.rowcount > 0
    connection.close()
    return success

#update a user
def update_user_by_id(user_id, first_name, last_name, email):
    """
    Updates a user's first name, last name, and email by their user ID.

    Args:
        user_id (int): The user's ID.
        first_name (str): The new first name.
        last_name (str): The new last name.
        email (str): The new email address.

    Returns:
        bool: True if the update was successful, False if the user wasn't found.
    """
    connection = get_db_connection()
    cursor = connection.cursor()

    # Update the user's details in the database
    cursor.execute("""
        UPDATE users
        SET FirstName = ?, LastName = ?, Email = ?
        WHERE UserID = ?
    """, (first_name, last_name, email, user_id))
    
    # Commit and check if any row was updated
    connection.commit()
    row_count = cursor.rowcount
    connection.close()

    return row_count > 0

#getting ingredients for a recipe
def get_ingredients_with_amounts_by_recipe_id(recipe_id):
    """
    Retrieves a list of ingredients 
    
    Args:
        recipe_id (int): The ID of the recipe.
    
    Returns:
        list: A list of dictionaries each containing ingredient details.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # SQL query to join tables and fetch necessary fields
    cursor.execute("""
        SELECT i.Ingredients AS Ingredient, i.IngredientsId
        FROM Recipe_Ingredients_fact_table ri
        JOIN Ingredients i ON ri.IngredientsID = i.IngredientsId
        WHERE ri.RecipeId = ?
    """, (recipe_id,))
    
    # Fetch results and format them as a list of dictionaries
    ingredients = [
        {"Ingredient": row["Ingredient"], "IngredientsId": row["IngredientsId"]}
        for row in cursor.fetchall()
    ]
    
    connection.close()
    return ingredients

def get_instructions_by_recipe_title(recipe_title):
    """
    Retrieves a list of instructions 
    
    Args:
        recipe_title (str): The title of the recipe.
    
    Returns:
        list: A list of dictionaries each containing instruction details.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        # SQL query to join tables and fetch necessary fields
        cursor.execute("""
            SELECT I.StepCount,
                   I.Instructions
            FROM Instructions I
            LEFT JOIN Recipes R on I.RecipeID = R.RecipeID
            WHERE R.Title = ?
        """, (recipe_title,))
        
        # Fetch results and format them as a list of dictionaries
        instructions = [
            {"StepCount": row["StepCount"], "Instruction": row["Instruction"]}
            for row in cursor.fetchall()
        ]
        
        if not instructions:
            raise IndexError("No instructions found for this recipe.")
        
    except IndexError as e:
        return {"message": str(e)}
    finally:
        connection.close()
    
    return instructions

# Get ingredients, instructions, reviews and ratings for a recipe ID
def fetch_recipe(recipe_id):
    """
    Fetch a specific recipe by RecipeID, including ingredients, instructions, and reviews.
    """
    try:
        query = """
        SELECT
            r.RecipeID,
            r.Title,
            r.Description,
            r.CookingTime,
            r.Servings,
            r.ImageURL,
            GROUP_CONCAT(DISTINCT i.Ingredients, ', ') AS Ingredients,
            GROUP_CONCAT(DISTINCT ins.Instructions, '||') AS Instructions,
            GROUP_CONCAT(DISTINCT u.FirstName || ' ' || u.LastName || ': ' || rv.ReviewText || ' (Rating: ' || rv.Rating || ')', '||') AS Reviews
        FROM Recipes r
        LEFT JOIN Recipe_Ingredients_fact_table rif ON r.RecipeID = rif.RecipeID
        LEFT JOIN Ingredients i ON rif.IngredientsID = i.IngredientsID
        LEFT JOIN Instructions ins ON r.RecipeID = ins.RecipeID
        LEFT JOIN Reviews rv ON r.RecipeID = rv.RecipeID
        LEFT JOIN Users u ON rv.UserID = u.UserID
        WHERE r.RecipeID = ?
        GROUP BY r.RecipeID;
        """
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, (recipe_id,))
            recipe = cursor.fetchone()

        if not recipe:
            return None

        # Convert the result to a dictionary
        recipe_data = {
            "RecipeID": recipe["RecipeID"],
            "Title": recipe["Title"],
            "Description": recipe["Description"],
            "CookingTime": recipe["CookingTime"],
            "Servings": recipe["Servings"],
            "ImageURL": recipe["ImageURL"],
            "Ingredients": recipe["Ingredients"].split(', ') if recipe["Ingredients"] else [],
            "Instructions": recipe["Instructions"].split('||') if recipe["Instructions"] else [],
            "Reviews": recipe["Reviews"].split('||') if recipe["Reviews"] else []
        }

        return recipe_data

    except Exception as e:
        raise RuntimeError(f"Error fetching recipe: {e}")
