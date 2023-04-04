# Selecting rows from tables demo

import sqlite3

# Connect to the database
connect = sqlite3.connect("my_friends.db")

# Create a cursor object
c = connect.cursor()

# Execute SQL statement; returns a cursor object (an iterator) containing queried data
c.execute("SELECT * FROM friends")

# Iterate through individual rows of the cursor object and print
# for row in c:
#     print(row)

# Fetch all rows using .fetchall() and return as a list of tuples
print(c.fetchall())

# Fetch the 1st instance of a record using .fetchone()
# Assuming there are multiple identical entries
c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
print(c.fetchone())

# Fetch all records with closeness > 5 and sort it by closeness (lowest to highest)
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")
print(c.fetchall())

connect.commit()
connect.close()
