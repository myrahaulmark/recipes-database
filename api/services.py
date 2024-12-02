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

# Query the Review table for reviews matching the given RecipeID

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
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# FRONTEND QUERIES USED - don't delete
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# Get ingredients, instructions, reviews and ratings for a recipe ID - to be used for single recipe view pages
def fetch_recipe(recipe_id):
    """
    Fetch a specific recipe by RecipeID, including ingredients, instructions, and reviews.
    Deduplicate the ingredients, instructions, and reviews after fetching.
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
            (SELECT GROUP_CONCAT(i.Ingredients, ', ')
             FROM Recipe_Ingredients_fact_table rif
             JOIN Ingredients i ON rif.IngredientsID = i.IngredientsID
             WHERE rif.RecipeID = r.RecipeID) AS Ingredients,
            (SELECT GROUP_CONCAT(ins.Instructions, '||')
             FROM Instructions ins
             WHERE ins.RecipeID = r.RecipeID) AS Instructions,
            (SELECT GROUP_CONCAT(u.FirstName || ' ' || u.LastName || ': ' || rv.ReviewText || ' (Rating: ' || rv.Rating || ')', '||')
             FROM Reviews rv
             JOIN Users u ON rv.UserID = u.UserID
             WHERE rv.RecipeID = r.RecipeID) AS Reviews
        FROM Recipes r
        WHERE r.RecipeID = ?;
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
            "Ingredients": list(set(recipe["Ingredients"].split(', '))) if recipe["Ingredients"] else [],
            "Instructions": list(set(recipe["Instructions"].split('||'))) if recipe["Instructions"] else [],
            "Reviews": list(set(recipe["Reviews"].split('||'))) if recipe["Reviews"] else []
        }

        return recipe_data

    except Exception as e:
        raise RuntimeError(f"Error fetching recipe: {e}")
    

# Get random recipes in Appetizers with ingredients, instructions and reviews - to be used in the random generator section
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

# Get random recipes in soups with ingredients, instructions and reviews - to be used in the random generator section
def get_random_soup_recipes(limit=6):
    """
    Fetches up to `limit` random recipes from the 'Soups' category.
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
            c.CategoryName = 'Soups'
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
  
# Get random recipes in desserts with ingredients, instructions and reviews - to be used in the random generator section
def get_random_dessert_recipes(limit=6):
    """
    Fetches up to `limit` random recipes from the 'Desserts' category.
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
            c.CategoryName = 'Desserts'
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

# Get an appetizer recipe by a keyword in the title - to be copied for other categories and used for search bar
def search_appetizers_by_title(keyword):
    """
    Searches for appetizer recipes based on a keyword in the title.

    Args:
        keyword (str): The search term provided by the user.

    Returns:
        list: A list of dictionaries containing RecipeID, Title, and ImageURL.
    """
    query = """
    SELECT 
        r.RecipeID, 
        r.Title, 
        r.ImageURL 
    FROM 
        Recipes r
    JOIN 
        Category_Recipe_fact_table rcft ON r.RecipeID = rcft.RecipeID
    JOIN 
        Categories c ON rcft.CategoryID = c.CategoryID
    WHERE 
        c.CategoryName = 'Appetizers'
        AND r.Title LIKE ?
    LIMIT 5;
    """
    keyword_pattern = f"%{keyword}%"  # Add wildcard for partial matching
    connection = get_db_connection()
    results = connection.execute(query, (keyword_pattern,)).fetchall()
    connection.close()

    # Convert the results to a list of dictionaries
    return [{"RecipeID": row["RecipeID"], "Title": row["Title"], "ImageURL": row["ImageURL"]} for row in results]

# Get an soup recipe by a keyword in the title - to be copied for other categories and used for search bar
def search_soups_by_title(keyword):
    """
    Searches for soup recipes based on a keyword in the title.

    Args:
        keyword (str): The search term provided by the user.

    Returns:
        list: A list of dictionaries containing RecipeID, Title, and ImageURL.
    """
    query = """
    SELECT 
        r.RecipeID, 
        r.Title, 
        r.ImageURL 
    FROM 
        Recipes r
    JOIN 
        Category_Recipe_fact_table rcft ON r.RecipeID = rcft.RecipeID
    JOIN 
        Categories c ON rcft.CategoryID = c.CategoryID
    WHERE 
        c.CategoryName = 'Soups'
        AND r.Title LIKE ?
    LIMIT 5;
    """
    keyword_pattern = f"%{keyword}%"  # Add wildcard for partial matching
    connection = get_db_connection()
    results = connection.execute(query, (keyword_pattern,)).fetchall()
    connection.close()

    # Convert the results to a list of dictionaries
    return [{"RecipeID": row["RecipeID"], "Title": row["Title"], "ImageURL": row["ImageURL"]} for row in results]

# Get a dessert recipe by a keyword in the title - to be copied for other categories and used for search bar
def search_desserts_by_title(keyword):
    """
    Searches for dessert recipes based on a keyword in the title.

    Args:
        keyword (str): The search term provided by the user.

    Returns:
        list: A list of dictionaries containing RecipeID, Title, and ImageURL.
    """
    query = """
    SELECT 
        r.RecipeID, 
        r.Title, 
        r.ImageURL 
    FROM 
        Recipes r
    JOIN 
        Category_Recipe_fact_table rcft ON r.RecipeID = rcft.RecipeID
    JOIN 
        Categories c ON rcft.CategoryID = c.CategoryID
    WHERE 
        c.CategoryName = 'Desserts'
        AND r.Title LIKE ?
    LIMIT 5;
    """
    keyword_pattern = f"%{keyword}%"  # Add wildcard for partial matching
    connection = get_db_connection()
    results = connection.execute(query, (keyword_pattern,)).fetchall()
    connection.close()

    # Convert the results to a list of dictionaries
    return [{"RecipeID": row["RecipeID"], "Title": row["Title"], "ImageURL": row["ImageURL"]} for row in results]

# Search for recipes with a group of keywords - to be used on a page for search_by_ingredients 
def search_recipes_by_ingredients(keywords, limit=5, min_matches=2):
    """
    Searches recipes that contain at least a minimum number of the specified ingredients.

    Args:
        keywords (list): A list of ingredient keywords to search for.
        limit (int): The maximum number of results to return.
        min_matches (int): The minimum number of ingredients that must match.

    Returns:
        list: A list of dictionaries with RecipeID, Title, and ImageURL.
    """
    if not keywords:
        return []

    placeholders = ', '.join('?' for _ in keywords)  # Create placeholders dynamically
    query = f"""
    SELECT DISTINCT r.RecipeID, r.Title, r.ImageURL
    FROM Recipes r
    JOIN Recipe_Ingredients_fact_table rif ON r.RecipeID = rif.RecipeID
    JOIN Ingredients i ON rif.IngredientsID = i.IngredientsID
    WHERE LOWER(i.Ingredients) IN (LOWER(?), LOWER(?), LOWER(?))
    GROUP BY r.RecipeID
    HAVING COUNT(DISTINCT i.Ingredients) >= ?
    LIMIT ?;
    """

    connection = get_db_connection()
    results = connection.execute(query, (*keywords, min_matches, limit)).fetchall()
    connection.close()

    return [{"RecipeID": row["RecipeID"], "Title": row["Title"], "ImageURL": row["ImageURL"]} for row in results]

#SUBMIT OR ADD A NEW RECIPE
def add_recipe_with_details(data):
    """
    Adds a recipe to the database along with its ingredients and instructions.
    """
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Add recipe to the Recipes table
        cursor.execute("""
            INSERT INTO Recipes (Title, Description, CookingTime, Servings, NumberOfSteps, NumberOfIngredients)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            data.get("Title", ""), 
            data.get("Description", ""), 
            data.get("CookingTime", 0), 
            data.get("Servings", 0), 
            len(data.get("Instructions", [])), 
            len(data.get("Ingredients", []))
        ))
        recipe_id = cursor.lastrowid

        # Add ingredients to the Ingredients table
        for ingredient in data.get("Ingredients", []):
            cursor.execute("""
                INSERT INTO Ingredients (Ingredients)
                VALUES (?)
            """, (ingredient.get("name", ""),))
            ingredient_id = cursor.lastrowid

            # Link recipe and ingredient
            cursor.execute("""
                INSERT INTO Recipe_Ingredients_fact_table (RecipeID, IngredientsID)
                VALUES (?, ?)
            """, (recipe_id, ingredient_id))

        # Add instructions to the Instructions table
        for step_count, instruction in enumerate(data.get("Instructions", []), start=1):
            cursor.execute("""
                INSERT INTO Instructions (RecipeID, StepCount, Instructions)
                VALUES (?, ?, ?)
            """, (recipe_id, step_count, instruction))

        connection.commit()
        return recipe_id

    except Exception as e:
        connection.rollback()
        raise e

    finally:
        connection.close()
