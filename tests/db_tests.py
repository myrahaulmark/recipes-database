import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the necessary modules from api.services
from api.services import get_categories, get_recipe_count_by_category, get_all_users

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

def get_all_users_test():
    print("Testing get_all_users function...")
    users = get_all_users()
    if users:
        print("Users found:")
        print(users)
    else:
        print("No users found or there was an issue retrieving data.")




# Call the test functions
if __name__ == "__main__":
    get_recipe_count_by_category_test()
    get_categories_test()
    