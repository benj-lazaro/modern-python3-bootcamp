print("...rock...")
print("...paper...")
print("...scissors...")
player_1 = input("Player 1, make your move: ")

print("*** NO CHEATING ***\n\n" * 30)

player_2 = input("Player 2, make your move: ")
print("SHOOT!")

if player_1 == player_2:
    print("It's a tie!")
elif player_1 == "rock":
    if player_2 == "scissors":
        print("Player 1 wins!")
    elif player_2 == "paper":
        print("Player 2 wins!")
elif player_1 == "paper":
    if player_2 == "rock":
        print("Player 1 wins!")
    elif player_1 == "scissors":
        print("Player 2 wins!")
elif player_1 == "scissors":
    if player_2 == "paper":
        print("Player 1 wins!")
    elif player_2 == "rock":
        print("Player 2 wins!")
else:
    print("Something went wrong.")
