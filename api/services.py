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

def get_categories() -> List[Category]:
    """
    Retrieves all categories from the database.

    Returns:
        List[Category]: A list of Category objects.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Categories")  # Make sure this matches your actual table name
    rows = cursor.fetchall()
    connection.close()

    # Map rows to Category objects
    categories = []
    for row in rows:
        # Create a Category object by passing individual fields (assuming the table columns are in order)
        category = Category(
            CategoryID=row["CategoryID"],  # Or row[0] if row is tuple
            CategoryName=row["CategoryName"]  # Or row[1] if row is tuple
        )
        categories.append(category)

    return categories

def get_reviews_for_recipe(recipe_id):
    # Query the Review table for reviews matching the given RecipeID
    return session.query(Review).filter(Review.RecipeID == recipe_id).all()

# Call the function to find a recipe with reviews
recipe_with_reviews = session.query(Recipe.RecipeID).select_from(Recipe).join(Review, Recipe.RecipeID == Review.RecipeID).first()

# If a recipe with reviews exists, query its reviews
if recipe_with_reviews:
    recipe_id = recipe_with_reviews.RecipeID
    reviews = get_reviews_for_recipe(recipe_id)

    if reviews:
        for review in reviews:
            print(f"Review: {review.ReviewText}, Rating: {review.Rating}")
    else:
        print(f"No reviews found for RecipeID {recipe_id}")
else:
    print("No recipes with reviews found.")

def get_average_rating_per_recipe():
    return session.query(Recipe.RecipeID, Recipe.Title, func.avg(Review.Rating).label('average_rating')).join(
        Review, Recipe.RecipeID == Review.RecipeID).group_by(Recipe.RecipeID).all()

# call to get the average rating for each recipe
average_ratings = get_average_rating_per_recipe()
for recipe_id, title, avg_rating in average_ratings:
    print(f"Recipe: {title}, Average Rating: {avg_rating}")



