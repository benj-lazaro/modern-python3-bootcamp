# Rock Paper Scissors Improved Version
from random import randint

human_player_wins = 0
computer_player_wins = 0
winning_score = 2

while human_player_wins < winning_score and computer_player_wins < winning_score:
    print(f"Human Score: {human_player_wins}, Computer Score: {computer_player_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")

    human_player = input("(Enter your choice): ").lower()
    if human_player == "quit" or human_player == "q":
        break

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
            human_player_wins += 1
        else:
            print("Computer wins!")
            computer_player_wins += 1
    elif human_player == "paper":
        if computer_player == "rock":
            print("You win!")
            human_player_wins += 1
        else:
            print("Computer wins!")
            computer_player_wins += 1
    elif human_player == "scissors":
        if computer_player == "paper":
            print("You win!")
            human_player_wins += 1
        else:
            print("Computer wins!")
            computer_player_wins += 1
    else:
        print("Something went wrong.")

if human_player_wins > computer_player_wins:
    print("Congrats! You won!")
elif human_player_wins == computer_player_wins:
    print("It's a tie.")
else:
    print("Oh no, the computer won.")

print(f"Final Score: Human: {human_player_wins}, Computer: {computer_player_wins}")