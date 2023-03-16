# Writing to a text file
# 'w' mode = write and overwrite previous content (if there's one) on the specified file
# Writes content to the specified file in the first parameter of .write("<filename>", "<mode>")
# The with statement eliminates the need to manually close the file

with open("haiku.txt", "w") as text_file:
    text_file.write("Here's one more haiku.\n")
    text_file.write("What about the older one?\n")
    text_file.write("Let's go and check it out.")

with open("lol.txt", "w") as text_file:
    text_file.write("hahaha\n" * 10000)
