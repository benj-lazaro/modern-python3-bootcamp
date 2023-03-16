# Write a function called statistics
# Takes in a filename
# Returns a dictionary with the number lines, words and characters in the file

def statistics(data_file):
    """statistics(file) returns the number of lines, words and characters of the passed file."""
    with open(data_file) as data:
        content = data.read()

        line_count = len(content.split("\n"))
        word_count = len(content.split())
        char_count = 0

        for char in content:
            if not char.isspace():
                char_count += 1

        return f"Lines: {line_count}, Words: {word_count}, Characters: {char_count}"


print(statistics("data.txt"))
