import sqlite3
import pandas as pd

# Step 1: Connect to the SQLite database
connection = sqlite3.connect('my_recipes.db')
cursor = connection.cursor()

# Step 3: Load data into the table
# Example data - Replace with your data source
data = [
    ('5000000', '3', 'This recipe is okay.', '2024-09-12', '900000', '3000004'),
    ('5000001', '4', 'This recipe is great!', '2024-09-12', '900003', '3000005'),
    ('5000002', '5', 'I loved this recipe!', '2024-09-12', '900000', '3000006'),
    ('5000003', '1', 'This food sucks!', '2024-09-12', '900005', '3000007'),
    ('5000004', '5', 'This recipe is... in a word, awful.', '2024-09-12', '900004', '3000008'),    
]
# Step 4: Insert data into the table
cursor.executemany('''
INSERT INTO Reviews (ReviewID, Rating, ReviewText, ReviewDate, UserID, RecipeID) VALUES (?, ?, ?, ?, ?, ?)
''', data)

# Step 5: Commit the transaction and close the connection
connection.commit()
connection.close()

print("Data loaded successfully.")

