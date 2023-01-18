# Ask for user input
# Duplicate user input
# Cease duplicating user input when safe word is given

user_response = str(input("Hey, how's it going? "))
safe_word = "stop copying me"

while user_response != safe_word:
    user_response = str(input(f"{user_response} \n"))

print("Ugh! Fine. You win.")
