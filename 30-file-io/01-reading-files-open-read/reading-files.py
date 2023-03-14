# Reading text files
# open() = opens a file & then returns a file object
# Python reads files using a cursor

text_file = open("story.txt")
print(text_file.read())         # Returns the entire content of text file
print(text_file.read())         # Returns blank due to the cursor moved to the end of the file after reading
