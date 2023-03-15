# Reading text files using the with statement
# Does NOT require the file handler to be closed with close()

with open("story.txt") as text_file:
    content = text_file.read()


print(content)              # Prints the content of the file
print(text_file.closed)     # Returns True; confirming that the file is properly closed
