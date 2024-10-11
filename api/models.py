# In this file, the classes that represent the data in our application are defined.

class Category:
    
    def __init__(self, category_id: int, category_name: str):
        self.category_id = category_id
        self.category_name = category_name
        
    def __repr__(self):
        return f'<Category {self.category_id} - {self.category_name}>'
    
    def to_dict(self):
        return {
            'category_id': self.category_id,
            'category_name': self.category_name
        }

def create_category_from_dict(data: dict) -> Category:
    return Category(data['category_id'], data['category_name'])

class User:
    
    def __init__(self, user_id: int, first_name: str, last_name: str, email: str, join_date: str):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.join_date = join_date
        
    def __repr__(self):
        return f'<User {self.user_id} - {self.first_name} {self.last_name}>'
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'join_date': self.join_date
        }

def create_user_from_dict(data: dict) -> User:
    return User(data['user_id'], data['first_name'], data['last_name'], data['email'], data['join_date'])

class Recipe:
    
    def __init__(self, recipe_id: int, title: str, description: str, cooking_time: int, servings: int, number_of_steps: int, submitted_date: str, number_of_ingredients: int, image_url: str):
        self.recipe_id = recipe_id
        self.title = title
        self.description = description
        self.cooking_time = cooking_time
        self.servings = servings
        self.number_of_steps = number_of_steps
        self.submitted_date = submitted_date
        self.number_of_ingredients = number_of_ingredients
        self.image_url = image_url
        
    def __repr__(self):
        return f'<Recipe {self.recipe_id} - {self.title}>'
    
    def to_dict(self):
        return {
            'recipe_id': self.recipe_id,
            'title': self.title,
            'description': self.description,
            'cooking_time': self.cooking_time,
            'servings': self.servings,
            'number_of_steps': self.number_of_steps,
            'submitted_date': self.submitted_date,
            'number_of_ingredients': self.number_of_ingredients,
            'image_url': self.image_url
        }

def create_recipe_from_dict(data: dict) -> Recipe:
    return Recipe(data['recipe_id'], data['title'], data['description'], data['cooking_time'], data['servings'], data['number_of_steps'], data['submitted_date'], data['number_of_ingredients'], data['image_url'])

class Ingredient:
    
    def __init__(self, ingredients_id: int, ingredients: str, serving_size: int, calories: int, total_fat: int, saturated_fat: int, cholesterol: int, sodium: int, carbohydrate: int, fiber: int, sugars: int, protein: int, fat: int, caffeine: int, source: str, date: str, is_allergen: str, food_allergen_id: int, food: str, food_class: str, food_type: str, food_group: str, allergy_type: str):
        self.ingredients_id = ingredients_id
        self.ingredients = ingredients
        self.serving_size = serving_size
        self.calories = calories
        self.total_fat = total_fat
        self.saturated_fat = saturated_fat
        self.cholesterol = cholesterol
        self.sodium = sodium
        self.carbohydrate = carbohydrate
        self.fiber = fiber
        self.sugars = sugars
        self.protein = protein
        self.fat = fat
        self.caffeine = caffeine
        self.source = source
        self.date = date
        self.is_allergen = is_allergen
        self.food_allergen_id = food_allergen_id
        self.food = food
        self.food_class = food_class
        self.food_type = food_type
        self.food_group = food_group
        self.allergy_type = allergy_type
        
    def __repr__(self):
        return f'<Ingredient {self.ingredients_id} - {self.ingredients}>'
    
    def to_dict(self):
        return {
            'ingredients_id': self.ingredients_id,
            'ingredients': self.ingredients,
            'serving_size': self.serving_size,
            'calories': self.calories,
            'total_fat': self.total_fat,
            'saturated_fat': self.saturated_fat,
            'cholesterol': self.cholesterol,
            'sodium': self.sodium,
            'carbohydrate': self.carbohydrate,
            'fiber': self.fiber,
            'sugars': self.sugars,
            'protein': self.protein,
            'fat': self.fat,
            'caffeine': self.caffeine,
            'source': self.source,
            'date': self.date,
            'is_allergen': self.is_allergen,
            'food_allergen_id': self.food_allergen_id,
            'food': self.food,
            'food_class': self.food_class,
            'food_type': self.food_type,
            'food_group': self.food_group,
            'allergy_type': self.allergy_type
        }

def create_ingredient_from_dict(data: dict) -> Ingredient:
    return Ingredient(
        data['ingredients_id'], data['ingredients'], data['serving_size'], data['calories'], 
        data['total_fat'], data['saturated_fat'], data['cholesterol'], data['sodium'], 
        data['carbohydrate'], data['fiber'], data['sugars'], data['protein'], data['fat'], 
        data['caffeine'], data['source'], data['date'], data['is_allergen'], data['food_allergen_id'], 
        data['food'], data['food_class'], data['food_type'], data['food_group'], data['allergy_type']
    )

class RecipeIngredientsFact:
    
    def __init__(self, comp_id: int, recipe_id: int, ingredients_id: int, ingredients: str):
        self.comp_id = comp_id
        self.recipe_id = recipe_id
        self.ingredients_id = ingredients_id
        self.ingredients = ingredients
        
    def __repr__(self):
        return f'<RecipeIngredientsFact {self.comp_id}>'
    
    def to_dict(self):
        return {
            'comp_id': self.comp_id,
            'recipe_id': self.recipe_id,
            'ingredients_id': self.ingredients_id,
            'ingredients': self.ingredients
        }

def create_recipe_ingredients_fact_from_dict(data: dict) -> RecipeIngredientsFact:
    return RecipeIngredientsFact(
        data['comp_id'], data['recipe_id'], data['ingredients_id'], data['ingredients']
    )

class Review:
    
    def __init__(self, review_id: int, rating: int, review_text: str, review_date: str, user_id: int, recipe_id: int):
        self.review_id = review_id
        self.rating = rating
        self.review_text = review_text
        self.review_date = review_date
        self.user_id = user_id
        self.recipe_id = recipe_id
        
    def __repr__(self):
        return f'<Review {self.review_id} - {self.rating} stars>'
    
    def to_dict(self):
        return {
            'review_id': self.review_id,
            'rating': self.rating,
            'review_text': self.review_text,
            'review_date': self.review_date,
            'user_id': self.user_id,
            'recipe_id': self.recipe_id
        }

def create_review_from_dict(data: dict) -> Review:
    return Review(
        data['review_id'], data['rating'], data['review_text'], 
        data['review_date'], data['user_id'], data['recipe_id']
    )

class RecipeCategoryFact:
    
    def __init__(self, recipe_id: int, category_id: int):
        self.recipe_id = recipe_id
        self.category_id = category_id
        
    def __repr__(self):
        return f'<RecipeCategoryFact RecipeID: {self.recipe_id}, CategoryID: {self.category_id}>'
    
    def to_dict(self):
        return {
            'recipe_id': self.recipe_id,
            'category_id': self.category_id
        }

def create_recipe_category_fact_from_dict(data: dict) -> RecipeCategoryFact:
    return RecipeCategoryFact(data['recipe_id'], data['category_id'])
