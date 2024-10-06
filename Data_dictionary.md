# Data Dictionary

## Categories
| Column      | Data Type | Description                            | Notes |
|-------------|-----------|----------------------------------------|-------|
| CategoryID  | INTEGER   | Unique identifier for each category     | Primary Key |
| Categories  | TEXT      | Name or label for the category          |       |

## Ingredients
| Column           | Data Type | Description                                      | Notes |
|------------------|-----------|--------------------------------------------------|-------|
| IngredientsId    | INTEGER   | Unique identifier for each ingredient             | Primary Key |
| Ingredients      | TEXT      | Name of the ingredient                            |       |
| ServingSize      | INTEGER   | Recommended serving size for the ingredient (in grams) |       |
| Calories         | INTEGER   | Total calories per serving                        |       |
| TotalFat         | INTEGER   | Total fat content (in grams) per serving          |       |
| SaturatedFat     | INTEGER   | Saturated fat content (in grams) per serving      |       |
| Cholesterol      | INTEGER   | Cholesterol content (in milligrams) per serving   |       |
| Sodium           | INTEGER   | Sodium content (in milligrams) per serving        |       |
| Carbohydrate     | INTEGER   | Total carbohydrates (in grams) per serving        |       |
| Fiber            | INTEGER   | Dietary fiber content (in grams) per serving      |       |
| Sugars           | INTEGER   | Total sugar content (in grams) per serving        |       |
| Protein          | INTEGER   | Protein content (in grams) per serving            |       |
| Fat              | INTEGER   | Total fat content (in grams)                      |       |
| Caffeine         | INTEGER   | Caffeine content (in milligrams) per serving      |       |
| Source           | TEXT      | Source or origin of the ingredient                |       |
| Date             | TEXT      | Date the ingredient was added or last updated     |       |
| IsAllergen       | TEXT      | Indicates if the ingredient is a common allergen  |       |
| Food_allergen_ID | INTEGER   | Identifier linking to a specific allergen         |       |
| Food             | TEXT      | General food type                                |       |
| Food_Class       | TEXT      | Classification of the food (e.g., grain, vegetable, etc.) |       |
| Food_Type        | TEXT      | Type of food (e.g., organic, processed)           |       |
| Food_Group       | TEXT      | Food group (e.g., dairy, protein)                 |       |
| Allergy_Type     | TEXT      | Description of the specific allergy               |       |

## Recipes
| Column              | Data Type  | Description                                                | Notes                                                                 |
|---------------------|------------|------------------------------------------------------------|-----------------------------------------------------------------------|
| RecipeID            | INTEGER    | Unique identifier for each recipe                           | Primary Key                                                           |
| Title               | TEXT       | Name of the recipe                                          | Not Null                                                              |
| Description         | TEXT       | Brief description of the recipe                             |                                                                       |
| CookingTime         | INTEGER    | Time required to cook the recipe (in minutes)               |                                                                       |
| Servings            | INTEGER    | Number of servings the recipe yields                        |                                                                       |
| NumberOfSteps       | INTEGER    | Total number of steps to prepare the recipe                 |                                                                       |
| Instructions        | TEXT       | Detailed instructions for preparing the recipe              |                                                                       |
| SubmittedDate       | DATE       | Date the recipe was submitted                               | Default value                                                         |
| NumberOfIngredients | INTEGER    | Total number of ingredients used in the recipe              |                                                                       |
| ImageURL            | TEXT       | URL link to an image of the recipe                          |                                                                       |
| CategoryID          | INTEGER    | Foreign key referencing the `Categories` table              | References `Categories(CategoryID)`                                   |

## Reviews
| Column      | Data Type | Description                                  | Notes                    |
|-------------|-----------|----------------------------------------------|--------------------------|
| ReviewID    | INTEGER   | Unique identifier for each review             | Primary Key               |
| Rating      | INTEGER   | Rating of the recipe (1 to 5 stars)           |                          |
| ReviewText  | TEXT      | Text of the review                            |                          |
| ReviewDate  | DATE      | Date the review was submitted                 |                          |
| UserID      | INTEGER   | Foreign key linking to the user who submitted the review | References `Users(UserID)` |
| RecipeID    | INTEGER   | Foreign key linking to the reviewed recipe    | References `Recipes(RecipeID)` |

## Users
| Column      | Data Type | Description                                  | Notes                    |
|-------------|-----------|----------------------------------------------|--------------------------|
| UserID      | INTEGER   | Unique identifier for each user               | Primary Key               |
| FirstName   | TEXT      | User's first name                             |                          |
| LastName    | TEXT      | User's last name                              |                          |
| Email       | TEXT      | User's email address                          |                          |
| JoinDate    | DATE      | Date the user registered                      |                          |

## Recipe_Ingredients_fact_table
| Column        | Data Type | Description                                      | Notes                    |
|---------------|-----------|--------------------------------------------------|--------------------------|
| CompID        | INTEGER   | Unique identifier for the composition (join table) | Primary Key             |
| RecipeID      | INTEGER   | Foreign key referencing the `Recipes` table       | References `Recipes(RecipeID)` |
| IngredientsID | INTEGER   | Foreign key referencing the `Ingredients` table   | References `Ingredients(IngredientsID)` |
| Ingredients   | TEXT      | Name of the ingredient                            |                          |

## Instructions
| Column         | Data Type | Description                                  | Notes                    |
|----------------|-----------|----------------------------------------------|--------------------------|
| InstructionsID | INTEGER   | Unique identifier for each instruction step   | Primary Key               |
| StepCount      | INTEGER   | Order or number of the step                   |                          |
| Instructions   | TEXT      | Detailed description of the instruction       |                          |
