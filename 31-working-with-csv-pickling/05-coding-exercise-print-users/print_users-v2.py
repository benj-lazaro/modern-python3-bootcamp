# Write a function called print_users
# It prints out all of the first and last names in the user.csv
from csv import reader


def print_users():
    """print_users() prints out the first and last names of users stored in user.csv file."""
    with open("user.csv") as data:
        content_read = reader(data)
        next(content_read)                  # Skip the CSV header

        for user in content_read:
            print(f"{user[0]} {user[1]}")


print_users()
