# Fix the pre-written function called count_dolllar-signs()
def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count                    # Problem fix by applying correct indentation on this line of code


print(count_dollar_signs("$$$"))
