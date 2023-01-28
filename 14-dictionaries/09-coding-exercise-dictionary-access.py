# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:

# If retuned value from food == bakery_stock, print out how many is left
if food in bakery_stock:
    print(f"{food}: {bakery_stock[food]} left")
else:
	print(f"{food}: We don't make that")
