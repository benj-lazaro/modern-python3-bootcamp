# Write code tht loops over the list
# Adds all the string together to form one large combined string (no spaces in between)
# Combined string should be in all uppercase
# Save the string into the variable result

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
result = ""
list_index = 0

while list_index < len(sounds):
    result += str(sounds[list_index]).upper()
    list_index += 1

print(result)
