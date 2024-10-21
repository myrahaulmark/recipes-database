# Recipes Database

 ## Project Overview

In the spirit of the French culinary practice mise en place the primary purpose of this project will be to develop a recipe model that helps users organize and explore recipes with ease, just like the culinary practice of preparing ingredients in advance.  Users can browse, create, and manage recipes, track ingredients, and read or leave reviews. Whether the user is looking for new meal ideas or trying to organize favorite dishes, “La Mise en Place1” will make it simple to discover and share recipes, with a focus on efficiency and good preparation. 

When the site is finished... 

Users will be able to easily search, browse, and filter recipes based on ingredients, dietary preferences, and cooking times. 

Users will be able to create and manage their own recipes, including uploading images, listing ingredients, and providing step-by-step instructions.2 

Users will have the ability to leave reviews and ratings, helping others discover popular and highly rated dishes. 

The system will efficiently organize recipes with features like ingredient tracking, allergen alerts, and category sorting, making meal planning easy and intuitive. 

 ## Installation
1. Clone the repository
2. Create virtual environment
```bash
python -m venv venv
```
3. Install the required packages
```bash
pip install -r requirements.txt
```
4. Load the sample data
```bash
python utility/load_data.py
```
## Running the application (TBD)
```bash
python run.py
```
The api will be accessible at (TBD))
## Features
- Add a recipe
- Review a recipe
- View reviews of a recipes
- View average rating of recipes
- View all recipes in a category

## Documentation
There is also an [API Documentation]() document that describes how to use the API. (TBD)
A [Data Dictionary](docs/Data_dictionary.md) document is also available that describes the fields in the database.
A [list of tables](docs/Diagram.md) is also available.


### Recommended Responsibilities for Each File:
`models.py`: Data models represent tables within the my_recipes database.

`services.py`: Contains all developed queries. 
git remote add origin https://github.com/myrahaulmark/recipe_db_project.git

Andrew's Queries:

Query 1: Users a left join and parameterized inputs to allow the user to pick a recipe to pull ingredients for.
Query 2: Allows the user to count how many recipes are allergen friendly.
Query 3: Pulls all the user information.

Myra's Queries:

Query 1: This query retrieves a list of recipes along with their ingredients based on a user-specified category. It dynamically accepts a category name as input, making it flexible for users to filter results by category. If the category does not exist, it prompts the user with a list of available categories.

Query 2: This query retrieves reviews for a specific recipe, using a parameterized input for recipe ID. This is useful for retrieving all reviews associated with a particular recipe based on user input.

Query 3: This query calculates the average rating for each recipe. It provides a summary of how users have rated different recipes, which is useful for understanding overall user satisfaction.