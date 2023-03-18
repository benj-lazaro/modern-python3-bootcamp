# Write a function called write_user
# It accepts two argument values: first name and last name
# Searches for the matching user in user.csv
# If found, returns the index of the matching user
# Otherwise, returns a string that the user is not found

from csv import reader


def find_user(first_name, last_name):
    with open("users.csv") as data:
        content = reader(data)

        for (index, row) in enumerate(content):
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]

            if first_name_match and last_name_match:
                return index

        return f"{first_name} {last_name} not found."


# Test Code
print(find_user("Colt", "Steele"))
print(find_user("Grace", "Hopper"))
print(find_user("Alan", "Turing"))
print(find_user("Haruna", "Iikubo"))
