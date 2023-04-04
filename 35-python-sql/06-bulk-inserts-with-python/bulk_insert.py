# Bulk insert demo

import sqlite3

# Establish connection to database
connection = sqlite3.connect("my_friends.db")

# Create a cursor object
c = connection.cursor()

# Bulk data
people = [
    ("Roald", "Anderson", 5),
    ("Rosa", "Parks", 8),
    ("Henry", "Hudson", 7),
    ("Neil", "Armstrong", 7),
    ("Daniel", "Boone", 3)
]

# Perform bulk inserts using .executemany() method
c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

# ALTERNATIVE
# Insert records individually and perform another tasks after each insert

# average = 0
# for person in people:
#     c.execute("INSERT INTO friends VALUES (?,?,?)", person)
#     print("Inserting now...")
#     average += person[2]    # Referring to the integer value
# print(average / len(people))

# Commit SQL inserts
connection.commit()

# Terminate database connection
connection.close()
