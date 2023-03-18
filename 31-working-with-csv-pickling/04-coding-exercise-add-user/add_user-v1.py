# Write a function called add_user()
# Takes two arguments: a first name and last name
# Use the information to add a new user to the existing csv file user.csv

from csv import DictWriter


def add_user(first_name, last_name):
    """add_user(str, str) adds the passed argument values to the user.csv file."""
    with open("user.csv", "a") as content:
        headers = ["First Name", "Last Name"]
        write_content = DictWriter(content, fieldnames=headers)
        write_content.writerow({
            "First Name": first_name,
            "Last Name": last_name
        })
        print(f"User {first_name} added to user.csv...")


add_user("Dwayne", "Johnson")
add_user("Haruna", "Iikubo")
