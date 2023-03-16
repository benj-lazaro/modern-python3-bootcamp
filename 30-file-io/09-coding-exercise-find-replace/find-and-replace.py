# Write a function called find_and_replace
# It takes in a file name, a word to search for and a replacement word
# It replaces all instances of the word in the file with the replacement word

def find_and_replace(data_file, target_text, replacement_text):
    """find_and_replace(file, string, string) updates the content of a file with the replacement text."""
    with open(data_file) as data:
        content = data.read()
        content_update = content.replace(target_text, replacement_text)

    with open(data_file, "w") as data:
        data.write(content_update)

    print("File updated...")


find_and_replace("data.txt", "text", "content")
