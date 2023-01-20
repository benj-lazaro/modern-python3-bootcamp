# Iterating list items using a for loop
print("Iterating list items using a for loop")
numbers = [1, 2, 3, 4]

for number in numbers:
    print(number)

colors = ["purple", "teal", "magenta"]
for color in colors:
    print(color)


# Iterating list items using a while loop
print("\nIterating list items using a while loop")
number_list = [1, 2, 3, 4]
list_index = 0

while list_index < len(number_list):
    print(number_list[list_index])
    list_index += 1

color_list = ["purple", "teal", "magenta", "crimson", "emerald"]
list_index = 0

while list_index < len(color_list):
    print(f"{list_index}: {color_list[list_index]}")
    list_index += 1
