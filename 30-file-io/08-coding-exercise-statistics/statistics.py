# Write a function called statistics
# Takes in a filename
# Returns a dictionary with the number lines, words and characters in the file

def statistics(data_file):
    """statistics(file) returns a dictionary containing no. lines, words and characters of the passed file."""
    with open(data_file) as data:
        content = data.read()

        line_count = len(content)
        word_count = len(content.split())
        char_count = 0

        for char in content:
            if not char.isspace():
                char_count += 1

        return {
            "Lines": line_count,
            "Words": word_count,
            "Characters": char_count
        }


print(statistics("data.txt"))
