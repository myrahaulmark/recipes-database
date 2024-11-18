import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the necessary modules from api.services
from api.services import fetch_recipe, get_categories, get_recipe_count_by_category, get_all_users, search_appetizers_by_title

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

def fetch_recipes_test(recipe_id):
    """
    Test the fetch_recipe function with the test database.
    Prints the recipe details for the given RecipeID.
    """
    try:
        # Fetch recipe using the provided RecipeID
        recipe = fetch_recipe(3000000)
        
        if recipe:
            print("Recipe Details:")
            print(f"RecipeID: {recipe['RecipeID']}")
            print(f"Title: {recipe['Title']}")
            print(f"Description: {recipe['Description']}")
            print(f"Cooking Time: {recipe['CookingTime']} minutes")
            print(f"Servings: {recipe['Servings']}")
            print(f"Image URL: {recipe['ImageURL']}")
            print("\nIngredients:")
            for ingredient in recipe['Ingredients']:
                print(f"- {ingredient}")
            print("\nInstructions:")
            for step in recipe['Instructions']:
                print(f"- {step}")
            print("\nReviews:")
            for review in recipe['Reviews']:
                print(f"- {review}")
        else:
            print(f"No recipe found for RecipeID: {recipe_id}")
    
    except Exception as e:
        print(f"Error during testing: {e}")



#test search for appetizer by keyword
def test_search_appetizers_by_title():
    """
    Test the search_appetizers_by_title function with a sample keyword.
    """
    # Sample keyword to search
    keyword = "cheese"

    # Perform the search
    results = search_appetizers_by_title(keyword)

    # Print the results
    print(f"Search results for keyword '{keyword}':")
    for recipe in results:
        print(f"RecipeID: {recipe['RecipeID']}, Title: {recipe['Title']}, ImageURL: {recipe['ImageURL']}")

# Call the test functions
if __name__ == "__main__":
    get_recipe_count_by_category_test()
    get_categories_test()

if __name__ == "__main__":
    fetch_recipes_test(3000000)  # Replace with a valid RecipeID from your test_db 

if __name__ == "__main__":
    test_search_appetizers_by_title()
