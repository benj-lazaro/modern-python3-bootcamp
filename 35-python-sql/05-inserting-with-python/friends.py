# Database connection demo
import sqlite3

# Access an existing database or create a new database if non-existent
conn = sqlite3.connect("my_friends.db")

# Create a cursor object; it serves as a temporary workspace for SQL commands
c = conn.cursor()

# Execute SQL statement passed into the cursor object as argument value using .execute() method
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

# Insert a new row into a table
# insert_query = '''INSERT INTO friends VALUES ('Merryweather', 'Lewis', 7);'''
# c.execute(insert_query)

# Better way of inserting a record into a table; prevents SQL injection
# form_first_name = "Mary-Todd"
# query = f"INSERT INTO friends (first_name) VALUES (?)"
# c.execute(query, (form_first_name,))

# Takes data from a form (Simulated) and inserts to corresponding columns accordingly in a table
data = ("Steve", "Irwin", 9)
query = "INSERT INTO friends VALUES (?, ?, ?)"
c.execute(query, data)

# Commit changes into the database
conn.commit()

# Terminate database connection
conn.close()
