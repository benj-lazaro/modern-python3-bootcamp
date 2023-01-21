# Basic syntax of slice / slicing list and/or strings
# list_name[start:end:step] -> similar to range()

print("Slicing")
number_list = [1, 2, 3, 4, 5]

print("\nStart slice at index 1 using [1:]")
print(number_list)
print(number_list[1:])

print("\nStart slice at index 3 using [3:]")
print(number_list)
print(number_list[3:])

print("\nStart slice at index -1 using [-1:]")
print(number_list)
print(number_list[-1:])

print("\nStart slice at index -3 using [-3:]")
print(number_list)
print(number_list[-3:])

print("\nStart slice at index 20 using [20:]")
print(number_list)
print(number_list[20:])


color_list = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
print("\nSlice from index 2 to the end using [2:]")
print(f"{color_list}")
print(f"{color_list[2:]}")

# Creating a copy of a list
print("\nCreate a copy of a list using [:]")
colors2 = color_list[:]
print(f"color_list = {color_list}")
print(f"colors2 = {colors2}")

print("\nVerify if both list contain identical items")
print(colors2 == color_list)

print("Verify if both list are the same i.e. stored identical locations in memory")
print(colors2 is color_list)


# Slice a list using a start & (exclusive) end index
print("\nSlice list with start & exclusive end index")

print("\nSlice from index 1 to (exclusive) index 3 using [1: 3]")
print(color_list)
print(color_list[1: 3])

# Negative index = how many list items to exclude from the end
print("\nSlice last two items from the list using [:-2]")
print(color_list)
print(color_list[: -2])

print("\nSlice first item & last item from the list using [1:-1]")
print(color_list)
print(color_list[1: -1])

print("\nSlice from 'red' to (including) 'blue' using [0: 5] or [:5]")
print(color_list)
print(color_list[0: 5])
print(color_list[: 5])

print("\nSlice from 'yellow' to 'green' using [2: 4]")
print(color_list)
print(color_list[2: 4])


# Slice a list using a start, (exclusive) end index and step value
print("\nSlice list with start, exclusive end index and step value")

# Slice from the start and every 3rd step item of the list using [::3]
print("\nSlice from start & every 3rd item of the list using [::3]")
print(color_list)
print(color_list[::3])

# Slice from index 1 until the end and every 2nd step item of the list using [1::2]
print("\nSlice from index 1 until the end every 2nd step item of the list using [1::2]")
print(color_list)
print(color_list[1::2])

# Slice using negative index reverses the order
print("\nSlice from index 1 until the end and every -1 step using [1::-1]")
print(color_list)
print(color_list[1::-1])

print("\nSlice from index 1 until the end and every -1 step using [2::-1]")
print(color_list)
print(color_list[2::-1])

print("\nSlice from index 1 until the end and every -1 step using [:1:-1]")
print(color_list)
print(color_list[:1:-1])

# Tricks with slices
print("\nReversing a string using slice [::-1]")
string_text = "This is fun!"
print(f"{string_text}")
print(f"{string_text[::-1]}")

print("\nModify specific portions of a list by inserting new items using [1:3]")
number_list = [1, 2, 3, 4, 5]
print(f"{number_list}")
number_list[1:3] = ['a', 'b', 'c']
print(f"{number_list}")

print("\nReverse the 5th item value in the list item using [5][::-1]")
print(f"{color_list}")
print(f"{color_list[5][::-1]}")