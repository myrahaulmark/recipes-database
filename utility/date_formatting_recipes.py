import sqlite3
from datetime import datetime

# Define a function to update date format
def update_date_format():
    # Connect to your SQLite database
    conn = sqlite3.connect("P:\\MABA\\Seminar\\recipes database\\my_recipes.db")
    cursor = conn.cursor()

    # Fetch all rows from the Recipes table (adjust the column names as needed)
    cursor.execute("SELECT RecipeID, SubmittedDate FROM Recipes")
    rows = cursor.fetchall()

    for row in rows:
        recipe_id = row[0]
        original_date = row[1]

        # Try to convert the date
        try:
            # Assume the original date is in 'MM/DD/YYYY' format
            new_date = datetime.strptime(original_date, '%m/%d/%Y').strftime('%Y-%m-%d')

            # Update the row with the new date format
            cursor.execute("""
                UPDATE Recipes
                SET SubmittedDate = ?
                WHERE RecipeID = ?
            """, (new_date, recipe_id))

            print(f"Updated Recipe ID {recipe_id}: {original_date} -> {new_date}")

        except ValueError:
            print(f"Skipping Recipe ID {recipe_id}: Invalid date format '{original_date}'")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Call the function to execute the updates
update_date_format()
