# Entity-Relationship Diagram

## Users
- **UserID** (PK)
- FirstName
- LastName
- Email
- JoinDate

## Categories
- **CategoryID** (PK)
- CategoryName

## Recipes
- **RecipeID** (PK)
- Title
- Description
- CookingTime
- Servings
- NumberOfSteps
- Instructions
- SubmittedDate
- NumberOfIngredients
- ImageURL

## Instructions
- **InstructionID** (PK)
- StepCount
- Instructions
- **RecipeID** (FK)

## Recipe Category Fact Table
- **RecipeID** (FK)
- **CategoryID** (FK)

## Reviews
- **ReviewID** (PK)
- Rating (1 to 5 stars)
- ReviewText
- ReviewDate
- **UserID** (FK)
- **RecipeID** (FK)

## Ingredients
- **IngredientID** (PK)
- Ingredients
- ServingSize
- Calories
- TotalFat
- SaturatedFat
- Cholesterol
- Sodium
- Carbohydrate
- Fiber
- Sugars
- Protein
- Fat
- Caffeine
- Source
- Date
- IsAllergen
- Food_allergen_ID
- Food
- Food_Class
- Food_Type
- Food_Group
- Allergy_Type

## Recipe Ingredients Fact Table
- **CompID** (PK)
- **RecipeID** (FK)
- **IngredientID** (FK)
