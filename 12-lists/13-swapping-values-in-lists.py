# To swap items in a list
# Often used when shuffling, sorting items & algorithm-specific swaps
name_list = ["James", "Michelle"]

print("Swapping items in a list")
print(name_list)
name_list[0], name_list[1] = name_list[1], name_list[0]
print(name_list)