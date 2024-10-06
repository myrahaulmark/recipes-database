from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Date, Float, func
from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy.ext.declarative import declarative_base

# Define the base class for models
Base = declarative_base()

# -----------------------------
# Table Definitions (Models)
# -----------------------------

# Categories Table
class Category(Base):
    __tablename__ = 'categories'
    
    CategoryID = Column(Integer, primary_key=True, autoincrement=True)
    CategoryName = Column(String)

# Users Table
class User(Base):
    __tablename__ = 'users'
    
    UserID = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String)
    LastName = Column(String)
    Email = Column(String)
    JoinDate = Column(Date)

# Recipes Table
class Recipe(Base):
    __tablename__ = 'recipes'
    
    RecipeID = Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String)
    Description = Column(String)
    CookingTime = Column(Integer)
    Servings = Column(Integer)
    NumberOfSteps = Column(Integer)
    SubmittedDate = Column(Date)
    NumberOfIngredients = Column(Integer)
    Image_url = Column(String)

# Ingredients Table
class Ingredient(Base):
    __tablename__ = 'ingredients'
    
    IngredientsID = Column(Integer, primary_key=True, autoincrement=True)
    Ingredients = Column(String, nullable=False)
    ServingSize = Column(Integer)
    Calories = Column(Integer)
    TotalFat = Column(Integer)
    SaturatedFat = Column(Integer)
    Cholesterol = Column(Integer)
    Sodium = Column(Integer)
    Carbohydrate = Column(Integer)
    Fiber = Column(Integer)
    Sugars = Column(Integer)
    Protein = Column(Integer)
    Fat = Column(Integer)
    Caffeine = Column(Integer)
    Source = Column(String)
    Date = Column(String)
    IsAllergen = Column(String)
    Food_allergen_ID = Column(Integer)
    Food = Column(String)
    Food_Class = Column(String)
    Food_type = Column(String)
    Food_Group = Column(String)
    Allergy_Type = Column(String)

# Recipe_Ingredients Fact Table (Many-to-Many relationship between Recipes and Ingredients)
class RecipeIngredientsFact(Base):
    __tablename__ = 'recipe_ingredients_fact_table'
    
    CompID = Column(Integer, primary_key=True, autoincrement=True)
    RecipeID = Column(Integer, ForeignKey('recipes.RecipeID'))
    IngredientsID = Column(Integer, ForeignKey('ingredients.IngredientsID'))
    Ingredients = Column(String)

# Reviews Table
class Review(Base):
    __tablename__ = 'reviews'
    
    ReviewID = Column(Integer, primary_key=True, autoincrement=True)
    Rating = Column(Integer)
    ReviewText = Column(String)
    ReviewDate = Column(Date)
    UserID = Column(Integer, ForeignKey('users.UserID'))
    RecipeID = Column(Integer, ForeignKey('recipes.RecipeID'))

# Recipe_Categories (Many-to-Many relationship between Recipes and Categories)
class RecipeCategory(Base):
    __tablename__ = 'recipe_categories'
    
    CategoryID = Column(Integer, ForeignKey('categories.CategoryID'), primary_key=True)
    RecipeID = Column(Integer, ForeignKey('recipes.RecipeID'), primary_key=True)

# -----------------------------
# Initialize the Database
# -----------------------------
engine = create_engine('sqlite:///recipes.db')
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# ---------------------------------------------------------
# QUERY FUNCTIONS (Joins, Parameterized Input, Aggregation)
# ---------------------------------------------------------

# 1. Query to get all recipes along with their ingredients (Join Query)
def get_recipes_with_ingredients():
    return session.query(Recipe, Ingredient, RecipeIngredientsFact).join(
        RecipeIngredientsFact, Recipe.RecipeID == RecipeIngredientsFact.RecipeID).join(
        Ingredient, RecipeIngredientsFact.IngredientsID == Ingredient.IngredientsID).all()

# 2. Query to get reviews for a specific recipe (Parameterized Input)
def get_reviews_for_recipe(recipe_id):
    return session.query(Review).filter(Review.RecipeID == recipe_id).all()

# 3. Query to get the average rating for each recipe (Aggregated Data)
def get_average_rating_per_recipe():
    return session.query(Recipe.RecipeID, Recipe.Title, func.avg(Review.Rating).label('average_rating')).join(
        Review, Recipe.RecipeID == Review.RecipeID).group_by(Recipe.RecipeID).all()

# ---------------------------------------------------------
# Example Calls to Query Functions (Controller-like usage)
# ---------------------------------------------------------

if __name__ == "__main__":
    # Example: Get all recipes with their ingredients (Join)
    recipes_with_ingredients = get_recipes_with_ingredients()
    for recipe, ingredient, _ in recipes_with_ingredients:
        print(f"Recipe: {recipe.Title}, Ingredient: {ingredient.Ingredients}")

    # Example: Get reviews for a specific recipe (Parameterized Input)
    recipe_id = 1  # Example RecipeID
    reviews = get_reviews_for_recipe(recipe_id)
    for review in reviews:
        print(f"Review: {review.ReviewText}, Rating: {review.Rating}")

    # Example: Get the average rating for each recipe (Aggregation)
    average_ratings = get_average_rating_per_recipe()
    for recipe_id, title, avg_rating in average_ratings:
        print(f"Recipe: {title}, Average Rating: {avg_rating}")
