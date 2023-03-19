# Write a function called delete_users
# Takes in a first name and last name
# Search the passed arguments values from the file users.csv
# Delete the matching entry
# Return a count on how many users were removed

from csv import reader, writer


def delete_users(first_name, last_name):
    """delete_users(str, str) deletes matching arguments values from the users.csv file."""
    with open("users.csv") as data:
        read_content = list(reader(data))                       # Store read content into a list

    user_delete_count = 0

    with open("users.csv", "w") as data:
        write_content = writer(data)

        for row in read_content:
            if row[0] == first_name and row[1] == last_name:    # If a match is found, write nothing on the file
                user_delete_count += 1                          # Increment delete count
            else:
                write_content.writerow(row)                     # Otherwise, write previously read content

    return f"User(s) deleted: {user_delete_count}"


# Test Code
print(delete_users("Colt", "Steele"))
print(delete_users("Alan", "Turing"))
