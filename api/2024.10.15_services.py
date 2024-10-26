import sqlite3
from models import User, Category, Recipe, Ingredient, RecipeCategoryFact, RecipeIngredientsFact, Review, Instruction
from typing import List
from pathlib import Path
import pandas as pd

def get_db_connection():
    """
    Establishes and returns a connection to the SQLite database.
    The connection uses 'data/my_recipes.db' as the database file and sets the
    row factory to sqlite3.Row, allowing access to columns by name.

    Returns:
        sqlite3.Connection: A connection object to the SQLite database.
    """
    DATABASE_PATH = Path(__file__).parents[1] / "data"
    connection = sqlite3.connect(DATABASE_PATH / 'my_recipes.db')
    connection.row_factory = sqlite3.Row  # This allows you to access columns by name
    return connection

# List all recipe categories
from models import Category  # Assuming Category is defined in models.py

def get_categories() -> List[Category]:
    """
    Retrieves all categories from the database.

    Returns:
        List[Category]: A list of Category objects.
    """
    # Establish a database connection
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Execute the query to fetch categories from the database
    cursor.execute("SELECT * FROM Categories")  # Make sure this matches your actual table name
    rows = cursor.fetchall()  # Fetch all rows from the query
    
    # Close the connection
    connection.close()

    # Map rows to Category objects
    categories = []
    for row in rows:
        # Create a Category object by passing individual fields (assuming the table columns are in order)
        category = Category(
            CategoryID=row["CategoryID"],  # Or row[0] if row is a tuple
            CategoryName=row["CategoryName"]  # Or row[1] if row is a tuple
        )
        categories.append(category)

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

#Number of recipes avaialble in each category
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


#pull the full list of users
def get_users():
    """
    Retrieves the full list of users.
    """
    connection = get_db_connection()
    cursor = connection.cursor()

    # Execute the query to show all users
    cursor.execute("""
        SELECT * FROM Users
    """)
    results = cursor.fetchall()
    connection.close()

#    for row in results:
#        print(dict(row))

    return results

get_users()

'''
def get_instructions_for_recipe():
    """
    Retrieves the instructions for a given recipe by recipe name.
    """
    recipe_name = input("Enter the recipe name: ")
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        SELECT I.StepCount, I.Instructions
        FROM Instructions I
        LEFT JOIN Recipes R on I.RecipeID = R.RecipeID
        WHERE R.Title = ?
    """
    Query1 = pd.read_sql_query(query, connection, params=(recipe_name,))
    connection.close()
    if Query1.empty:
        print(f"No records found for recipe: {recipe_name}.") #I cannot add the recipe name in the output window
    else:
        print(Query1)
    return Query1


# Call the function
get_instructions_for_recipe()
'''

def count_allergens():
    """
    Counts allergens.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
        SELECT Count(IngredientsID) as count, IsAllergen
        FROM Ingredients
        GROUP BY IsAllergen
    ''')
    
    results = cursor.fetchall()
    connection.close()
    
    if results:
        for row in results:
            print(dict(row))
    else:
        print("No results found.")
    
    return results

count_allergens() #Counts allergens

