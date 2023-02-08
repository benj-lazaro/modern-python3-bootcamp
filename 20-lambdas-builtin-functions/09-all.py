# all = returns True if ALL elements of an iterable are truthy or empty
print("all():")

number_list = [1, 2, 3]
print(f"number_list: {number_list}")
print("Statement: all(number_list)")
print(f"Result: {all(number_list)}")

number_list = [0, 1, 2, 3]
print(f"\nnumber_list: {number_list}")
print("Statement: all(number_list)")
print(f"Result: {all(number_list)}")

vowel_list = ["a", "e", "i", "o", "u"]
print(f"\nvowel_list: {vowel_list}")
print("Statement: all([char for char in 'eio' if char in vowel_list])")
print(f"Result: {all([char for char in 'eio' if char in vowel_list])}")
print("Statement: all(['eio' for char in vowel_list])")
print(f"Result: {all(['eio' for char in vowel_list])}")

number_list = [4, 2, 10, 6, 8]
print(f"\nnumber_list: {number_list}")
print("Stetement: all([number for number in number_list if number % 2 == 0])")
print(f"Result: {all([number for number in number_list if number % 2 == 0])}")
print("Statement: all([number % 2 == 0 for number in number_list])")
print(f"Result: {all([number % 2 == 0 for number in number_list])}")

people_list = ["Charlie", "Casey", "Cody", "Carly", "Christina"]
print(f"\npeople_list: {people_list}")
print("Statement: all([person for person in people_list if person[0] == 'C')")
print(f"Result: {all([person for person in people_list if person[0] == 'C'])}")
print("Stataement: all([person[0] == 'C' for person in people_list])")
print(f"Result: {all([person[0] == 'C' for person in people_list])}")
