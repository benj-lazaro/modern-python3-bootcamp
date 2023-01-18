print("...rock...")
print("...paper...")
print("...scissors...")
player_1 = input("Player 1, make your move: ")

print("*** NO CHEATING ***\n\n")
print("*** NO CHEATING ***\n\n")
print("*** NO CHEATING ***\n\n")
print("*** NO CHEATING ***\n\n")
print("*** NO CHEATING ***\n\n")
print("*** NO CHEATING ***\n\n")
print("*** NO CHEATING ***\n\n")
print("*** NO CHEATING ***\n\n")
print("*** NO CHEATING ***\n\n")
print("*** NO CHEATING ***\n\n")

player_2 = input("Player 2, make your move: ")
print("SHOOT!")

if player_1 == "rock" and player_2 == "scissors":
    print("Player 1 wins!")
elif player_1 == "rock" and player_2 == "paper":
    print("Player 2 wins!")
elif player_1 == "paper" and player_2 == "rock":
    print("Player 1 wins!")
elif player_1 == "paper" and player_2 == "scissors":
    print("Player 2 wins!")
elif player_1 == "scissors" and player_2 == "paper":
    print("Player 1 wins!")
elif player_1 == "scissors" and player_2 == "rock":
    print("Player 2 wins!")
elif player_1 == player_2:
    print("It's a tie!")
else:
    print("Something went wrong.")
