# Write a function called copy_and_reverse
# It takes in a file name of an existing file as well as a file name for another to be created
# It copies, then reverses the content before writing to the 2nd file

def copy_and_reverse(original_file, new_file):
    """copy(file, file) copies the content of the 1st file and reverses it to the 2nd file."""
    with open(original_file) as original:
        content = original.read()

    with open(new_file, "w") as new:
        new.write(content[::-1])

    print("Copy and reverse operation done.")


copy_and_reverse("original.txt", "duplicate.txt")
