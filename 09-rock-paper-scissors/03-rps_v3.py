from random import randint

print("...rock...")
print("...paper...")
print("...scissors...")
human_player = input("(Enter your choice): ").lower()

# Simulated rudimentary basic AI
random_number = randint(0, 2)
if random_number == 0:
    computer_player = "rock"
elif random_number == 1:
    computer_player = "paper"
else:
    computer_player = "scissors"

print(f"The computer plays: {computer_player}")

if human_player == computer_player:
    print("It's a tie.")
elif human_player == "rock":
    if computer_player == "scissors":
        print("You win!")
    else:
        print("Computer wins!")
elif human_player == "paper":
    if computer_player == "rock":
        print("You win!")
    else:
        print("Computer wins!")
elif human_player == "scissors":
    if computer_player == "paper":
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Something went wrong.")
