# In this file, the classes that represent the data in our application are defined.

class Category:
    
    def __init__(self, CategoryID: int, CategoryName: str):
        self.CategoryID = CategoryID
        self.CategoryName = CategoryName
        
    def __repr__(self):
        return f'<Category {self.CategoryID} - {self.CategoryName}>'
    
    def to_dict(self):
        return {
            'CategoryID': self.CategoryID,
            'CategoryName': self.CategoryName
        }

def create_category_from_dict(data: dict) -> Category:
    return Category(data['CategoryID'], data['CategoryName'])


class User:
    
    def __init__(self, UserID: int, FirstName: str, LastName: str, Email: str, JoinDate: str):
        self.UserID = UserID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.JoinDate = JoinDate
        
    def __repr__(self):
        return f'<User {self.UserID} - {self.FirstName} {self.LastName}>'
    
    def to_dict(self):
        return {
            'UserID': self.UserID,
            'FirstName': self.FirstName,
            'LastName': self.LastName,
            'Email': self.Email,
            'JoinDate': self.JoinDate
        }

def create_user_from_dict(data: dict) -> User:
    return User(data['UserID'], data['FirstName'], data['LastName'], data['Email'], data['JoinDate'])


class Recipe:
    
    def __init__(self, RecipeID: int, Title: str, Description: str, CookingTime: int, Servings: int, NumberOfSteps: int, Instructions: str, SubmittedDate: str, NumberOfIngredients: int, ImageURL: str):
        self.RecipeID = RecipeID
        self.Title = Title
        self.Description = Description
        self.CookingTime = CookingTime
        self.Servings = Servings
        self.NumberOfSteps = NumberOfSteps
        self.Instructions = Instructions
        self.SubmittedDate = SubmittedDate
        self.NumberOfIngredients = NumberOfIngredients
        self.ImageURL = ImageURL
        
    def __repr__(self):
        return f'<Recipe {self.RecipeID} - {self.Title}>'
    
    def to_dict(self):
        return {
            'RecipeID': self.RecipeID,
            'Title': self.Title,
            'Description': self.Description,
            'CookingTime': self.CookingTime,
            'Servings': self.Servings,
            'NumberOfSteps': self.NumberOfSteps,
            'Instructions': self.Instructions,
            'SubmittedDate': self.SubmittedDate,
            'NumberOfIngredients': self.NumberOfIngredients,
            'ImageURL': self.ImageURL
        }

def create_recipe_from_dict(data: dict) -> Recipe:
    return Recipe(data['RecipeID'], data['Title'], data['Description'], data['CookingTime'], data['Servings'], data['NumberOfSteps'], data['Instructions'], data['SubmittedDate'], data['NumberOfIngredients'], data['ImageURL'])

class Ingredient:
    
    def __init__(self, IngredientID: int, Ingredients: str, ServingSize: int, Calories: int, TotalFat: int, SaturatedFat: int, Cholesterol: int, Sodium: int, Carbohydrate: int, Fiber: int, Sugars: int, Protein: int, Fat: int, Caffeine: int, Source: str, Date: str, IsAllergen: str, Food_allergen_ID: int, Food: str, Food_Class: str, Food_Type: str, Food_Group: str, Allergy_Type: str):
        self.IngredientID = IngredientID
        self.Ingredients = Ingredients
        self.ServingSize = ServingSize
        self.Calories = Calories
        self.TotalFat = TotalFat
        self.SaturatedFat = SaturatedFat
        self.Cholesterol = Cholesterol
        self.Sodium = Sodium
        self.Carbohydrate = Carbohydrate
        self.Fiber = Fiber
        self.Sugars = Sugars
        self.Protein = Protein
        self.Fat = Fat
        self.Caffeine = Caffeine
        self.Source = Source
        self.Date = Date
        self.IsAllergen = IsAllergen
        self.Food_allergen_ID = Food_allergen_ID
        self.Food = Food
        self.Food_Class = Food_Class
        self.Food_Type = Food_Type
        self.Food_Group = Food_Group
        self.Allergy_Type = Allergy_Type
        
    def __repr__(self):
        return f'<Ingredient {self.IngredientID} - {self.Ingredients}>'
    
    def to_dict(self):
        return {
            'IngredientID': self.IngredientID,
            'Ingredients': self.Ingredients,
            'ServingSize': self.ServingSize,
            'Calories': self.Calories,
            'TotalFat': self.TotalFat,
            'SaturatedFat': self.SaturatedFat,
            'Cholesterol': self.Cholesterol,
            'Sodium': self.Sodium,
            'Carbohydrate': self.Carbohydrate,
            'Fiber': self.Fiber,
            'Sugars': self.Sugars,
            'Protein': self.Protein,
            'Fat': self.Fat,
            'Caffeine': self.Caffeine,
            'Source': self.Source,
            'Date': self.Date,
            'IsAllergen': self.IsAllergen,
            'Food_allergen_ID': self.Food_allergen_ID,
            'Food': self.Food,
            'Food_Class': self.Food_Class,
            'Food_Type': self.Food_Type,
            'Food_Group': self.Food_Group,
            'Allergy_Type': self.Allergy_Type
        }

def create_ingredient_from_dict(data: dict) -> Ingredient:
    return Ingredient(
        data['IngredientID'], data['Ingredients'], data['ServingSize'], data['Calories'], 
        data['TotalFat'], data['SaturatedFat'], data['Cholesterol'], data['Sodium'], 
        data['Carbohydrate'], data['Fiber'], data['Sugars'], data['Protein'], data['Fat'], 
        data['Caffeine'], data['Source'], data['Date'], data['IsAllergen'], data['Food_allergen_ID'], 
        data['Food'], data['Food_Class'], data['Food_Type'], data['Food_Group'], data['Allergy_Type']
    )


class RecipeIngredientsFact:
    
    def __init__(self, CompID: int, RecipeID: int, IngredientID: int):
        self.CompID = CompID
        self.RecipeID = RecipeID
        self.IngredientID = IngredientID
        
    def __repr__(self):
        return f'<RecipeIngredientsFact {self.CompID}>'
    
    def to_dict(self):
        return {
            'CompID': self.CompID,
            'RecipeID': self.RecipeID,
            'IngredientID': self.IngredientID
        }

def create_recipe_ingredients_fact_from_dict(data: dict) -> RecipeIngredientsFact:
    return RecipeIngredientsFact(data['CompID'], data['RecipeID'], data['IngredientID'])

class Review:
    
    def __init__(self, ReviewID: int, Rating: int, ReviewText: str, ReviewDate: str, UserID: int, RecipeID: int):
        self.ReviewID = ReviewID
        self.Rating = Rating
        self.ReviewText = ReviewText
        self.ReviewDate = ReviewDate
        self.UserID = UserID
        self.RecipeID = RecipeID
        
    def __repr__(self):
        return f'<Review {self.ReviewID} - {self.Rating} stars>'
    
    def to_dict(self):
        return {
            'ReviewID': self.ReviewID,
            'Rating': self.Rating,
            'ReviewText': self.ReviewText,
            'ReviewDate': self.ReviewDate,
            'UserID': self.UserID,
            'RecipeID': self.RecipeID
        }

def create_review_from_dict(data: dict) -> Review:
    return Review(data['ReviewID'], data['Rating'], data['ReviewText'], data['ReviewDate'], data['UserID'], data['RecipeID'])


class RecipeCategoryFact:
    
    def __init__(self, RecipeID: int, CategoryID: int):
        self.RecipeID = RecipeID
        self.CategoryID = CategoryID
        
    def __repr__(self):
        return f'<RecipeCategoryFact RecipeID: {self.RecipeID}, CategoryID: {self.CategoryID}>'
    
    def to_dict(self):
        return {
            'RecipeID': self.RecipeID,
            'CategoryID': self.CategoryID
        }

def create_recipe_category_fact_from_dict(data: dict) -> RecipeCategoryFact:
    return RecipeCategoryFact(data['RecipeID'], data['CategoryID'])

class Instruction:
    
    def __init__(self, InstructionID: int, StepCount: int, Instructions: str, RecipeID: int):
        self.InstructionID = InstructionID
        self.StepCount = StepCount
        self.Instructions = Instructions
        self.RecipeID = RecipeID
        
    def __repr__(self):
        return f'<Instruction {self.InstructionID} - Step {self.StepCount}>'
    
    def to_dict(self):
        return {
            'InstructionID': self.InstructionID,
            'StepCount': self.StepCount,
            'Instructions': self.Instructions,
            'RecipeID': self.RecipeID
        }

def create_instruction_from_dict(data: dict) -> Instruction:
    return Instruction(data['InstructionID'], data['StepCount'], data['Instructions'], data['RecipeID'])
