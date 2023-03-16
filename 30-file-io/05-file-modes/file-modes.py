# Modes for opening files
# "r" = reads content from an existing file, default mode
# "w" = writes content to a file, overwrite previous content of the file
# "a" = appends content at the end of a file, previous content preserved; seek() does NOT work as intended
# "r+" = reads from and writes/overwrites content to an exiting file at the beginning; seek() works here

# Add new content at the end of the text file
with open("haiku.txt", "a") as text_file:
    text_file.write(" Appending new content later!\n")

# Intends to add new content at the beginning of the file
# However, it is using "a" that does NOT work with seek()
with open("haiku.txt", "a") as text_file:
    text_file.seek(0)
    text_file.write(":)\n")

# Attempts to add a new content at the beginning of the file using "r+"
# NOTE: "r+" will NOT create a file that does NOT exist
with open("haiku.txt", "r+") as text_file:
    text_file.write("I was here first!")
    text_file.seek(10)                              # Move cursor 10 steps from the beginning
    text_file.write(" *** Kilroy was here *** ")
