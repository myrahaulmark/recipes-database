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


# Get all categories
def get_categories() -> List[dict]:
    """
    Retrieves all categories from the database.

    Returns:
        List[dict]: A list of dictionaries representing categories.
    """
    # Establish a database connection
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Execute the query to fetch categories from the database
    cursor.execute("SELECT CategoryID, CategoryName FROM Categories")  # Ensure this matches your actual table name
    rows = cursor.fetchall()  # Fetch all rows from the query
    
    # Map rows to Category objects
    categories = []
    for row in rows:
        # Create a Category object by passing individual fields (assuming the table columns are in order)
        category = Category(
            CategoryID=row["CategoryID"],
            CategoryName=row["CategoryName"]
        )
        categories.append(category.to_dict())  # Use to_dict() for JSON compatibility

    # Close the connection
    connection.close()

    return categories


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
