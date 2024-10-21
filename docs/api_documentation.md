
# Recipe Database API Documentation

This document provides an overview of the API routes for managing recipes, users, ingredients, categories, and instructions. These routes are part of a RESTful API that allows creating, updating, deleting, and retrieving information about recipes and related entities.

## Base URL
The base URL for all the routes is `/api`.

## Endpoints

### Home Endpoint

- **URL**: `/`
- **Method**: `GET`
- **Summary**: Displays a welcome message for the API.
- **Response**:
  - `200 OK`: Welcome message.

---

### Connection Test

- **URL**: `/connection`
- **Method**: `GET`
- **Summary**: Test the connection to the API and database.
- **Response**:
  - `200 OK`: JSON response indicating successful connection.
  - **Example**: `{ "message": "Successfully connected to the API" }`

---

## User Endpoints

### Get All Users

- **URL**: `/users`
- **Method**: `GET`
- **Summary**: Retrieve all users.
- **Response**:
  - `200 OK`: List of users.

### Add a New User

- **URL**: `/users`
- **Method**: `POST`
- **Summary**: Add a new user to the system.
- **Request Body**:
  - **`username`**: User's username.
  - **`email`**: User's email.
- **Response**:
  - `201 Created`: User added successfully.

### Get User by ID

- **URL**: `/users/{user_id}`
- **Method**: `GET`
- **Summary**: Retrieve user information by user ID.
- **Parameters**:
  - **`user_id`**: The unique identifier of the user.
- **Response**:
  - `200 OK`: User found.
  - `404 Not Found`: User not found.

### Update User by ID

- **URL**: `/users/{user_id}`
- **Method**: `PUT`
- **Summary**: Update an existing user.
- **Parameters**:
  - **`user_id`**: The unique identifier of the user.
- **Request Body**:
  - **`username`**: User's new username.
  - **`email`**: User's new email.
- **Response**:
  - `200 OK`: User updated successfully.

### Delete User by ID

- **URL**: `/users/{user_id}`
- **Method**: `DELETE`
- **Summary**: Remove a user by their ID.
- **Parameters**:
  - **`user_id`**: The unique identifier of the user.
- **Response**:
  - `200 OK`: User deleted successfully.

---

## Recipe Endpoints

### Get All Recipes

- **URL**: `/recipes`
- **Method**: `GET`
- **Summary**: Retrieve all recipes or filter by title.
- **Parameters**:
  - **`title`** (optional): Filter recipes by title.
- **Response**:
  - `200 OK`: List of recipes.

### Add a New Recipe

- **URL**: `/recipes`
- **Method**: `POST`
- **Summary**: Add a new recipe to the system.
- **Request Body**:
  - **`title`**: Recipe title.
  - **`description`**: Recipe description.
  - **`cooking_time`**: Time required to cook the recipe.
  - **`servings`**: Number of servings.
- **Response**:
  - `201 Created`: Recipe added successfully.

### Get Recipe by ID

- **URL**: `/recipes/{recipe_id}`
- **Method**: `GET`
- **Summary**: Retrieve recipe information by recipe ID.
- **Parameters**:
  - **`recipe_id`**: The unique identifier of the recipe.
- **Response**:
  - `200 OK`: Recipe found.
  - `404 Not Found`: Recipe not found.

### Update Recipe by ID

- **URL**: `/recipes/{recipe_id}`
- **Method**: `PUT`
- **Summary**: Update an existing recipe.
- **Parameters**:
  - **`recipe_id`**: The unique identifier of the recipe.
- **Request Body**:
  - **`title`**: New title.
  - **`description`**: New description.
  - **`cooking_time`**: Updated cooking time.
  - **`servings`**: Updated servings.
- **Response**:
  - `200 OK`: Recipe updated successfully.

### Delete Recipe by ID

- **URL**: `/recipes/{recipe_id}`
- **Method**: `DELETE`
- **Summary**: Remove a recipe by its ID.
- **Parameters**:
  - **`recipe_id`**: The unique identifier of the recipe.
- **Response**:
  - `200 OK`: Recipe deleted successfully.

---

## Ingredient Endpoints

### Get All Ingredients

- **URL**: `/ingredients`
- **Method**: `GET`
- **Summary**: Retrieve all ingredients.
- **Response**:
  - `200 OK`: List of ingredients.

### Add a New Ingredient

- **URL**: `/ingredients`
- **Method**: `POST`
- **Summary**: Add a new ingredient to the system.
- **Request Body**:
  - **`name`**: Name of the ingredient.
- **Response**:
  - `201 Created`: Ingredient added successfully.

### Get Ingredient by ID

- **URL**: `/ingredients/{ingredient_id}`
- **Method**: `GET`
- **Summary**: Retrieve ingredient information by ingredient ID.
- **Parameters**:
  - **`ingredient_id`**: The unique identifier of the ingredient.
- **Response**:
  - `200 OK`: Ingredient found.
  - `404 Not Found`: Ingredient not found.

### Update Ingredient by ID

- **URL**: `/ingredients/{ingredient_id}`
- **Method**: `PUT`
- **Summary**: Update an existing ingredient.
- **Parameters**:
  - **`ingredient_id`**: The unique identifier of the ingredient.
- **Request Body**:
  - **`name`**: New name of the ingredient.
- **Response**:
  - `200 OK`: Ingredient updated successfully.

### Delete Ingredient by ID

- **URL**: `/ingredients/{ingredient_id}`
- **Method**: `DELETE`
- **Summary**: Remove an ingredient by its ID.
- **Parameters**:
  - **`ingredient_id`**: The unique identifier of the ingredient.
- **Response**:
  - `200 OK`: Ingredient deleted successfully.

---

## Category Endpoints

### Get All Categories

- **URL**: `/categories`
- **Method**: `GET`
- **Summary**: Retrieve all categories.
- **Response**:
  - `200 OK`: List of categories.

### Add a New Category

- **URL**: `/categories`
- **Method**: `POST`
- **Summary**: Add a new category to the system.
- **Request Body**:
  - **`name`**: Name of the category.
- **Response**:
  - `201 Created`: Category added successfully.

### Get Category by ID

- **URL**: `/categories/{category_id}`
- **Method**: `GET`
- **Summary**: Retrieve category information by category ID.
- **Parameters**:
  - **`category_id`**: The unique identifier of the category.
- **Response**:
  - `200 OK`: Category found.
  - `404 Not Found`: Category not found.

### Update Category by ID

- **URL**: `/categories/{category_id}`
- **Method**: `PUT`
- **Summary**: Update an existing category.
- **Parameters**:
  - **`category_id`**: The unique identifier of the category.
- **Request Body**:
  - **`name`**: New name of the category.
- **Response**:
  - `200 OK`: Category updated successfully.

### Delete Category by ID

- **URL**: `/categories/{category_id}`
- **Method**: `DELETE`
- **Summary**: Remove a category by its ID.
- **Parameters**:
  - **`category_id`**: The unique identifier of the category.
- **Response**:
  - `200 OK`: Category deleted successfully.

---

## Instruction Endpoints

### Get All Instructions for a Recipe

- **URL**: `/recipes/{recipe_id}/instructions`
- **Method**: `GET`
- **Summary**: Retrieve all instructions for a specific recipe.
- **Parameters**:
  - **`recipe_id`**: The unique identifier of the recipe.
- **Response**:
  - `200 OK`: List of instructions for the recipe.

### Add New Instruction for a Recipe

- **URL**: `/recipes/{recipe_id}/instructions`
- **Method**: `POST`
- **Summary**: Add a new instruction for a recipe.
- **Parameters**:
  - **`recipe_id`**: The unique identifier of the recipe.
- **Request Body**:
  - **`instruction`**: The instruction text.
- **Response**:
  - `201 Created`: Instruction added successfully.

---

# Schemas

### User
- **`id`**: integer, example: `1`
- **`username`**: string, example: `jane_doe`
- **`email`**: string, example: `jane.doe@example.com`

### Recipe
- **`recipe_id`**: integer, example: `1`
- **`title`**: string, example: `Spaghetti Bolognese`
- **`description`**: string, example: `A classic Italian pasta dish...`
- **`cooking_time`**: integer, example: `30`
- **`servings`**: integer, example: `4`

### Ingredient
- **`ingredient_id`**: integer, example: `1`
- **`name`**: string, example: `Tomato`

# Swagger UI Documentation

The API is documented using **Swagger UI**, which provides an interactive user interface to explore and test the API endpoints.

## Accessing Swagger UI
- **URL**: `http://localhost:5000/apidocs/`
- **Description**: Swagger UI provides a visual representation of the API routes, allowing you to send test requests and view the responses directly from the browser.

### Steps to Access Swagger UI
1. **Run the Flask application**: Start your server by running the `run.py` file:
   ```sh
   python run.py
   ```
2. **Open your browser**: Navigate to `http://localhost:5000/apidocs/` to see the Swagger UI.
3. **Interact with the API**: You can view all available endpoints, see the required parameters, and send requests to test each endpoint.

# Testing the API with Postman

You can also test the API endpoints using **Postman**, a tool for API development and testing.

## Steps to Use Postman:

1. **Download and install Postman**: If you don’t have it installed already, you can download it from [Postman’s official site](https://www.postman.com/downloads/).

2. **Set up a new request**:
    - Open Postman and click **New** > **HTTP Request**.
    - Enter the desired API endpoint (e.g., `http://localhost:5000/api/users`).

3. **Choose the method**: 
    - Select the appropriate HTTP method (GET, POST, PUT, DELETE) depending on what you want to do.
    - Example: Choose `GET` for fetching users or `POST` for creating a new recipe.

4. **Add headers (if needed)**: 
    - If your API requires authentication, add the necessary API key or authentication token in the headers.

5. **Send the request**: 
    - After configuring the endpoint, method, and any required data, click the **Send** button to submit your request and view the response.

6. **View responses**: 
    - Postman will display the API’s response, including status codes (e.g., 200 OK) and any returned data, in the interface.

7. **Optional**: You can save requests, organize them into collections, and even automate testing by using Postman collections.

## Example Requests:

- **GET** all users: `GET http://localhost:5000/api/users`
- **POST** a new recipe: `POST http://localhost:5000/api/recipes` (with recipe data in the request body)

