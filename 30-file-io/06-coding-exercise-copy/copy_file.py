# Write a function called copy
# It takes in a file name of an existing file as well as a file name for another to be created
# It copies the content of the 1st file to the 2nd file

def copy(original_file, new_file):
    """copy(file, file) copies the content of the 1st file to the 2nd file."""
    with open(original_file) as original:
        content = original.read()

    with open(new_file, "w") as new:
        new.write(content)

    print("Copy done.")


copy("original.txt", "duplicate.txt")
