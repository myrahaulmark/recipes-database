# How to use the API
This document would typically be a README.md in your repository, but since we used the README.md file to explain the three different API implementations, we are going to use this file as example documentation for each API.

## Basic Flask API

### Getting Started
To get started, you'll need to install the dependencies.  You can do this by running the following command:
```bash
pip install -r requirements.txt
```

### Running the API
To run the API, you can run the following command:
```bash
python basic-flask.py
```

### Using the API
Once the API is running, you can use the following commands to interact with it.

# Let's create a markdown file with the API documentation content provided.
markdown_content = """
# Recipe Database API Documentation

## API Overview
This documentation provides the available endpoints for the Recipe Database API.

**Host:** `http://localhost:5000/api`  
**Version:** `1.0.0`  

---

### Endpoints

#### Categories

- **Retrieve all recipe categories**
    - **URL:** `/categories`
    - **Method:** `GET`
    - **Description:** Fetches all available recipe categories.
    - **Response:**
        - `200 OK`: Returns a list of categories.
        - **Schema:**
            ```json
            [
                {
                    "CategoryID": 1,
                    "CategoryName": "Italian"
                }
            ]
            ```

#### Users

- **Retrieve users filtered by last name**
    - **URL:** `/users`
    - **Method:** `GET`
    - **Description:** Fetches a list of users based on a last name filter.
    - **Parameters:**
        - `name` (query, required): The string to filter last names by.  
          - Example: `Smith`
        - `starts_with` (query, optional): If `true`, filters users whose last names start with the provided string.
          - Default: `true`
    - **Response:**
        - `200 OK`: Returns a list of users matching the filter criteria.
        - **Schema:**
            ```json
            [
                {
                    "UserID": 1,
                    "FirstName": "John",
                    "LastName": "Smith",
                    "Email": "john.smith@example.com"
                }
            ]
            ```

- **Add a new user**
    - **URL:** `/users`
    - **Method:** `POST`
    - **Description:** Adds a new user to the database.
    - **Request Body:**
        ```json
        {
            "FirstName": "John",
            "LastName": "Doe",
            "Email": "johndoe@example.com"
        }
        ```
    - **Response:**
        - `201 Created`: User created successfully.

- **Delete a user**
    - **URL:** `/users/{UserID}`
    - **Method:** `DELETE`
    - **Description:** Deletes a user identified by `UserID`.
    - **Parameters:**
        - `UserID` (path, required): The ID of the user to delete.
    - **Response:**
        - `200 OK`: User deleted successfully.
        - `404 Not Found`: User not found.

- **Update an existing user**
    - **URL:** `/users/{UserID}`
    - **Method:** `PUT`
    - **Description:** Updates a user's details by UserID.
    - **Parameters:**
        - `UserID` (path, required): The ID of the user to update.
    - **Request Body:**
        ```json
        {
            "FirstName": "John",
            "LastName": "Doe",
            "Email": "john.doe@example.com"
        }
        ```
    - **Response:**
        - `200 OK`: User updated successfully.
        - `404 Not Found`: User not found.
        - `400 Bad Request`: Required fields missing in the request body.

#### Reviews

- **Retrieve reviews for a specific recipe**
    - **URL:** `/Reviews/{RecipeID}`
    - **Method:** `GET`
    - **Description:** Retrieves review information for a recipe identified by `RecipeID`.
    - **Parameters:**
        - `RecipeID` (path, required): The unique identifier of the recipe.
    - **Response:**
        - `200 OK`: Returns a list of reviews for the specified recipe.
        - **Schema:**
            ```json
            [
                {
                    "ReviewID": 1,
                    "RecipeID": 101,
                    "ReviewerName": "Jane Doe",
                    "ReviewText": "Delicious recipe, easy to follow!",
                    "Rating": 5,
                    "ReviewDate": "2023-10-10"
                }
            ]
            ```
        - `404 Not Found`: No reviews found for the specified RecipeID.

#### Ingredients

- **Retrieve ingredients for a specific recipe**
    - **URL:** `/ingredients/{recipe_id}`
    - **Method:** `GET`
    - **Description:** Fetches all ingredients for a given recipe ID.
    - **Parameters:**
        - `recipe_id` (path, required): The ID of the recipe to retrieve ingredients for.
    - **Response:**
        - `200 OK`: Returns a list of ingredients for the specified recipe.
        - **Schema:**
            ```json
            [
                {
                    "Ingredient": "Salt",
                    "IngredientsId": 101007,
                    "RecipeName": "Sample Recipe Name"
                }
            ]
            ```
        - `404 Not Found`: No ingredients found for the specified recipe.
"""


