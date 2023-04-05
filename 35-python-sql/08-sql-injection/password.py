# SQL injection demo = non-sanitized user inputs


import sqlite3

connection = sqlite3.connect("user.db")

username = str(input("Please enter your username: "))
user_password = str(input("Please enter your password: "))
cursor = connection.cursor()

# SQL injection string = ' OR 1=1 --
# The ' closes the password=' part of the SQL query
# The OR 1=1 makes the entire SQL query to be True
# The -- comments out the remaining part of the SQL query

# BAD SQL query = susceptible to simple SQL injection attack
# query = f"SELECT * FROM users WHERE username='{username}' AND password='{user_password}'"
# cursor.execute(query)

# Sanitized SQL query = sqlite3 library helps prevent simple SQL injections
query = f"SELECT * FROM users WHERE username=?  AND password=?"
cursor.execute(query, (username, user_password))

result = cursor.fetchone()

if result:
    print("Welcome back")
else:
    print("Failed login")

connection.commit()
connection.close()
