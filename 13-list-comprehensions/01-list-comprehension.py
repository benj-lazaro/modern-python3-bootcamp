# List comprehension basic syntax
# [<operation_done_on_each_item> for <each_item_in_iterable> in <iterable>]

number_list = [1, 2, 3, 4 ,5]
print(f"number_list: {number_list}")

print("\nMultiply each item in the number_list by 10")
result = [number * 10 for number in number_list]
print(f"Result: {result}")

print("\nMultiply each item in the number_list by 2")
result = [number * 2 for number in number_list]
print(f"Result: {result}")

print("\nDivide each item in the number_list by 2")
result = [number / 2 for number in number_list]
print(f"Result: {result}")

print("\nUppercase each character in the variable firstname")
firstname = "colt"
print(f"variable firstname: {firstname}")
result = [character.upper() for character in firstname]
result = "".join(result)
print(f"Result: {result}")

print("\nUppercase the first letter of each name in the friend_list")
friend_list = ["ashley", "matt", "michael"]
print(f"friend_list: {friend_list}")
result = [friend[0].upper() + friend[1:] for friend in friend_list]
print(f"Result: {result}")

print("\nMultiply each number by 10 in range(1, 6)")
result = [number * 10 for number in range(1, 6)]
print(f"Result: {result}")

print("\nIdentify the boolean value of each item in bool_list")
bool_list = [0, [], '', ' ', 1]
print(f"bool_list: {bool_list}")
result = [bool(item) for item in bool_list]
print(f"Result: {result}")

print("\nConvert each number in the number_list into string")
result = [str(number) for number in number_list]
print(f"number_list: {number_list}")
print(f"Result: {result}")

print("\nUppercase each color in the color_list")
color_list = ["orange", "yellow", "green", "blue", "indigo", "violet"]
print(f"color_list: {color_list}")
result = [color.upper() for color in color_list]
print(f"Result: {result}")

print("\nAppend the string 'Hello' to each number in the number_list")
result = [str(number)+"Hello" for number in number_list]
print(f"Result: {result}")
