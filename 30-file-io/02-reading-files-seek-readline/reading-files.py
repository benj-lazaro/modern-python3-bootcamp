# Reading text files
# seek() = moves the cursor (after the content of a file has been read)
# readline() = reads the file one line (row) at at time
# readlines() = reads all the lines (row) of a file but preserves each line as items in a list
# close() = closes the file
# .closed = returns True if the file has been closed; otherwise False

# read() demo
print("Opening the file...")
text_file = open("story.txt")   # Open targeted text file

print("\nReading file content...")
print(text_file.read())

print("\nReading file contents (w/o resetting cursor)...")
print(text_file.read())

print("\nResetting cursor to the beginning of the file...")
text_file.seek(0)

print("\nReading file content...")
print(text_file.read())

print("\nResetting cursor to index 1 (2nd character from the beginning) of the file...")
text_file.seek(1)

print("\nReading file content...")
print(text_file.read())

print("\nResetting cursor to index 50 (50th character from the beginning) of the file...")
text_file.seek(50)

print("\nReading file content...")
print(text_file.read())

# readline() demo
print("\nResetting cursor to the beginning of the file...")
text_file.seek(0)

print("\nReading the 1st line of the file content using readline()...")
print(text_file.readline())

print("\nReading the 2nd line of the file content using readline()...")
print(text_file.readline())

print("\nReading the 3rd line of the file content using readline()...")
print(text_file.readline())

print("\nReading beyond the end of the file content using readline()...")
print(text_file.readline())

# readlines() demo
print("\nResetting cursor to the beginning of the file...")
text_file.seek(0)

print("\nReading file contents using readlines()...")
print(text_file.readlines())

# Manually close the file
print("\nClosing the file with close()...")
text_file.close()

print("\nVeriying thet the file is closed....")
print(text_file.closed)

print("\nAttempting to read a closed file using read()...") # Triggers a ValueError: I/O operation on closed file
print(text_file.read())
