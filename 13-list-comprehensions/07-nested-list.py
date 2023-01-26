# Nested list syntax
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing nested list
print(f"nested_list: {nested_list}")
print(f"1st nested list's 2nd item: {nested_list[0][1]}")
print(f"2nd nested list's last item : {nested_list[1][-1]}")
print(f"3rd nested list's 2nd item : {nested_list[-1][1]}")

# Iterating through nested list
print("\nIterating through nested list")
for list_item_index in nested_list:
    for list_item_value in list_item_index:
        print(list_item_value)

# Iterate the pair & individual coordinates from the list
coordinates = [[10.243, 9.132], [37.212, -14.092], [21.367, 32.572]]

for coordinate_pair_value in coordinates:
    print(f"Location coordinates: {coordinate_pair_value}")
    for individual_coordinate in coordinate_pair_value:
        print(f"Coordinate: {individual_coordinate}")


# Nested list comprehension
print("\nNested list comprehension:")
print(f"nested_list: {nested_list}")

[[print(list_item_value) for list_item_value in list_item_index] for list_item_index in nested_list]

# Generate a 3x3 gameboard, filled with integers 1 to 3
print("\nGenerate a 3x3 TicTacToe board filled with integers from 1 to 3:")
game_board = [[number for number in range(1, 4)] for list_item_value in range(1, 4)]
print(game_board)

# Generate a 3x3 gameboard, filled with X on even-tiles and O on odd-tiles
print("Generate a 3x3 gameboard filled with X (even titles) & with O (odd tiles)")
print([["X" if number % 2 != 0 else "O" for number in range(1, 4)] for value in range(1, 4)])

# Generate a 3x3 gameboard filled with *
print("Generate a gameboard Filled with *")
print([["*" for item_index in range(1, 4)] for value in range(1, 4)])
