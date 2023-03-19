# Write a function called update_users
# Takes in an old first name, old last name, new first name and new last name
# Updates the contents of the users.csv
# Returns a count of how many users were update

from csv import reader, writer


def update_users(first_name, last_name, new_first_name, new_last_name):
    """update_users(str, str, str, str) search and update matching argument values. """

    with open("users.csv") as data:
        read_content = list(reader(data))

    with open("users.csv", "w") as data:
        write_content = writer(data)
        user_update_count = 0

        for row in read_content:
            if row[0] == first_name and row[1] == last_name:
                write_content.writerow([new_first_name, new_last_name])
                user_update_count += 1
            else:
                write_content.writerow(row)

    return f"User(s) updated: {user_update_count}"


# Test Code
print(update_users("Grace", "Hopper", "Haruna", "Iikubo"))
print(update_users("Colt", "Steele", "Boba", "Fett"))
print(update_users("Alan", "Turing", "Elon", "Musk"))
print(update_users("Chris", "Evas", "Robert", "Downey Jr."))
