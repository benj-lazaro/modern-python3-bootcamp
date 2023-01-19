from random import randint

# Ask the user to guess a number between 1 and 10
# Informs the user if the guessed number is higher or lower to the hidden randomize number

random_number = randint(1, 10)
continue_playing = True

while continue_playing:
    guessed_number = int(input("Guess a number between 1 and  10: "))

    if guessed_number < random_number:
        print("Too low, try again!")
    elif guessed_number > random_number:
        print("Too high, try again!")
    else:
        print("You guessed it! You won!")
        user_response = str(input("Do you want to keep playing (y/n): ")).lower()

        if user_response == "y":
            random_number = randint(1, 10)
        else:
            print("Thank you for playing!")
            continue_playing = False

