# Write a function called write_user
# It accepts two argument values: first name and last name
# Searches for the matching user in user.csv
# If found, returns the index of the matching user
# Otherwise, returns a string that the user is not found

from csv import DictReader


def find_user(first_name, last_name):
    """find_user(str, str) returns the index / row location of passed user first name & last name."""
    with open("users.csv") as data:
        content = DictReader(data)
        index_location = 0

        for row in content:
            index_location += 1
            if row["First Name"] == first_name and row["Last Name"] == last_name:
                return index_location

        return f"{first_name} {last_name} not found."


# Test Code
print(find_user("Colt", "Steele"))
print(find_user("Grace", "Hopper"))
print(find_user("Alan", "Turing"))
print(find_user("Haruna", "Iikubo"))
