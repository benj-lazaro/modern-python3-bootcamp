# Print an emoji art using a for & a while loop

# for loop version
print("for loop version")
for character in range(1, 11):
    print("\U0001f600" * character)

# while loop version
print("while loop version")
height_art = 1
while height_art < 11:
    print("\U0001f600" * height_art)
    height_art += 1

# for & while loop version = wonky approach
print("for & while loop version")
for num in range(1, 11):
    emoji_art = ""
    height_art = 1

    while height_art <= num:
        emoji_art += "\U0001f600"
        height_art += 1

    print(emoji_art)
