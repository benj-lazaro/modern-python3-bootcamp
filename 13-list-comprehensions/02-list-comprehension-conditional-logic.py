# List comprehension with conditional logic syntax
# [<list_item> for <list_item_in_iterable> in <iterable> if <conditional_Logic>]

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Collect even numbers from number_list")
print(f"number_list: {number_list}")
result = [number for number in number_list if number % 2 == 0]
print(f"Result: {result}")

print("\nCollect odd numbers from number_list")
print(f"number_list: {number_list}")
result = [number for number in number_list if number % 2 != 0]
print(f"Result: {result}")


# Alternative syntax
# [<list_item_operation> if <conditional_logic> else <else_operaiton> for <list_item> in <iterable>

print("\nMultiply the number by 2 if number is divisible by 2 else divide the number by 2")
print(f"number_list: {number_list}")
result = [number * 2 if number % 2 == 0 else number / 2 for number in number_list]
print(f"Result: {result}")

# To use in conjunction with .join()
print("\nRemove vowels from the string in variable with_vowels")
with_vowels = "This is so much fun!"
print(f"with_vowels: {with_vowels}")
result = ''.join(character for character in with_vowels if character not in 'aeiou')
print(f"Result: {result}")
