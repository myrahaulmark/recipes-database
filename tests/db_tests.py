import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the necessary modules from api.services
from api.services import get_db_connection, get_categories, get_recipe_count_by_category

def get_db_connection_test():
    cnn = get_db_connection()
    print(cnn)


def get_categories_test():
    categories = get_categories()
    print(categories)


def get_recipe_count_by_category_test():
    """
    Test the get_recipe_count_by_category function using the test database.
    """
    recipe_count = get_recipe_count_by_category()  # Call the correct function
    for row in recipe_count:
        category_name, recipe_count = row['CategoryName'], row['recipe_count']
        print(f"Category: {category_name}, Number of Recipes: {recipe_count}")


# Call the test functions
get_db_connection_test()
get_recipe_count_by_category_test()
get_categories_test()
