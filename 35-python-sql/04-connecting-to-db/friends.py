# Database connection demo
import sqlite3

# Access an existing database or create a new database if non-existent
conn = sqlite3.connect("my_friends.db")

# Create a cursor object; it serves as a temporary workspace for SQL commands
c = conn.cursor()

# Execute SQL statement passed into the cursor object as argument value using .execute() method
c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

# Commit changes into the database
conn.commit()

# Terminate database connection
conn.close()
