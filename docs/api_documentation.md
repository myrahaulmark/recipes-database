# User and Movie API Documentation

This document provides an overview of the API routes for managing recipes, users, instructions and ingredients. These routes are part of a RESTful API that allows creating, updating, deleting, and retrieving information about recipes and ingredients.

## Base URL
The base URL for all the routes is `/api`.
Here's a Markdown version of your OpenAPI specification:

## Endpoints

### Home Endpoint

- **URL**: `/`
- **Method**: `GET`
- **Summary**: Displays a welcome message for the API.
- **Response**:
  - `200 OK`: Welcome message.

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
- **Summary**: Retrieve all users or filter by name.
- **Parameters**:
  - **`starts_with`** (optional): Filter users whose names start with the given string.
  - **`contains`** (optional): Filter users whose names contain the given string.
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
  - **Example**: `{ "message": "User added", "user": { ... } }`

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

### Get All Ratings for a User

- **URL**: `/users/{user_id}/ratings`
- **Method**: `GET`
- **Summary**: Retrieve all ratings for a specific user.
- **Parameters**:
  - **`user_id`**: The unique identifier of the user.
- **Response**:
  - `501 Not Implemented`: Currently not implemented.
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


### Get Recipe by ID

- **URL**: `/movies/{movie_id}`
- **Method**: `GET`
- **Summary**: Retrieve movie information by movie ID.
- **Parameters**:
  - **`movie_id`**: The unique identifier of the movie.
- **Response**:
  - `200 OK`: Movie found.
  - `404 Not Found`: Movie not found.

### Update Movie by ID

- **URL**: `/movies/{movie_id}`
- **Method**: `PUT`
- **Summary**: Update an existing movie.
- **Parameters**:
  - **`movie_id`**: The unique identifier of the movie.
- **Request Body**:
  - **`title`**: New title.
  - **`genre`**: New genre.
  - **`release_year`**: New release year.
  - **`director`**: New director.
- **Response**:
  - `200 OK`: Movie updated successfully.

### Delete Recipe by ID

- **URL**: `/movies/{movie_id}`
- **Method**: `DELETE`
- **Summary**: Remove a movie by its ID.
- **Parameters**:
  - **`movie_id`**: The unique identifier of the movie.
- **Response**:
  - `200 OK`: Movie deleted successfully.

### Get All Ratings for a Recipe

- **URL**: `/movies/{movie_id}/ratings`
- **Method**: `GET`
- **Summary**: Retrieve all ratings for a specific movie by movie ID.
- **Parameters**:
  - **`movie_id`**: The unique identifier of the movie.
- **Response**:
  - `200 OK`: List of ratings for the movie.

---

## Rating Endpoints

### Add a New Rating

- **URL**: `/ratings`
- **Method**: `POST`
- **Summary**: Add a new rating to the system.
- **Request Body**:
  - **`user_id`**: ID of the user providing the rating.
  - **`movie_id`**: ID of the movie being rated.
  - **`rating`**: The rating score.
  - **`review`**: Text review.
- **Response**:
  - `201 Created`: Rating added successfully.

### Get Rating by ID

- **URL**: `/ratings/{rating_id}`
- **Method**: `GET`
- **Summary**: Retrieve rating information by rating ID.
- **Parameters**:
  - **`rating_id`**: The unique identifier of the rating.
- **Response**:
  - `200 OK`: Rating found.
  - `404 Not Found`: Rating not found.

### Update Rating by ID

- **URL**: `/ratings/{rating_id}`
- **Method**: `PUT`
- **Summary**: Update an existing rating.
- **Parameters**:
  - **`rating_id`**: The unique identifier of the rating.
- **Request Body**:
  - **`rating`**: New rating score.
  - **`review`**: New review text.
- **Response**:
  - `200 OK`: Rating updated successfully.

### Delete Rating by ID

- **URL**: `/ratings/{rating_id}`
- **Method**: `DELETE`
- **Summary**: Remove a rating by its ID.
- **Parameters**:
  - **`rating_id`**: The unique identifier of the rating.
- **Response**:
  - `200 OK`: Rating deleted successfully.

---

## Schemas

### User

- **`id`**: integer, example: `1`
- **`username`**: string, example: `jane_doe`
- **`email`**: string, example: `jane.doe@example.com`

### Recipe

- **`movie_id`**: integer, example: `1`
- **`title`**: string, example: `Inception`
- **`genre`**: string, example: `Sci-Fi`
- **`release_year`**: integer, example: `2010`
- **`director`**: string, example: `Christopher Nolan`

### Rating

- **`rating_id`**: integer, example: `101`
- **`user_id`**: integer, example: `1`
- **`movie_id`**: integer, example: `1`
- **`rating`**: float, example: `4.5`
- **`review`**: string, example: `Great movie, loved the plot!`

## Swagger UI Documentation

The API is documented using **Swagger UI**, which provides an interactive user interface to explore and test the API endpoints.

### Accessing Swagger UI
- **URL**: `http://localhost:5000/apidocs/`
- **Description**: Swagger UI provides a visual representation of the API routes, allowing you to send test requests and view the responses directly from the browser.

### Steps to Access Swagger UI
1. **Run the Flask application**: Start your server by running the `run.py` file:
   ```sh
   python run.py
   ```
2. **Open your browser**: Navigate to `http://localhost:5000/apidocs/` to see the Swagger UI.
3. **Interact with the API**: You can view all available endpoints, see the required parameters, and send requests to test each endpoint.

