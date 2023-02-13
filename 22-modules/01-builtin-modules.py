from random import choice, randint as magic_number_chooser, shuffle

fruit_list = ["apple", "banana", "cherry", "durian"]
print(f"fruit_list: {fruit_list}")
print(f"fruit_choice: {choice(fruit_list)}")

shuffle(fruit_list)
print(f"fruit_list: {fruit_list}")

print(f"random number: {magic_number_chooser(1, 100)}")
