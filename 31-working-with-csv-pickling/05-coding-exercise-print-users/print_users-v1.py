# Write a function called print_users
# It prints out all of the first and last names in the user.csv
from csv import DictReader


def print_users():
    with open("user.csv") as data:
        content = DictReader(data)

        for row in content:
            print(f"{row['First Name']} {row['Last Name']}")


print_users()
