# List methods index, count, sort, reverse, join

# .index() method = returns the index of the specified item (by value) in the list
print("Using .index() method")
crew_list = ["Rutherford", "Tendi", "Mariner", "Boimler"]
print(crew_list)
print(f"The name Tendi is located at index {crew_list.index('Tendi')}")

number_list = [5, 5, 6, 7, 5, 8, 8, 9, 10]
print(f"\n{number_list}")
# Look for the instance of item value 5 after index 1
print(f"The 1st instance of 5 starting at index 1 is located at index {number_list.index(5, 1)}")
print(f"The 1st instance of 5 starting at index 2 is located at index {number_list.index(5, 2)}")
print(f"The 1st instance of 8 between index 6 & 8 is located at index {number_list.index(8, 6, 8)}")

name_list = ["colt", "blue", "arya", "lena", "colt", "selena", "pablo"]
print(f"\n{name_list}")
print(f"The 1st instance of colt between index 1 & 6 is at index {name_list.index('colt', 1, 6)}")

# .count() method = returns the number of occurrence an item (by value) appears in a list
print("\nUsing .count() method")
name_list = ["colt", "blue", "arya", "lena", "colt", "selena", "pablo"]
print(f"{name_list}")
print(f"The item 'colt' appeared {name_list.count('colt')} time(s) in the list.")
print(f"The item 'selena' appeared {name_list.count('selena')} time(s) in the list.")

# .reverse() method = reverses the order of elements of the list (in-place)
print("\nUsing .reverset() method")
name_list = ["colt", "blue", "arya", "lena", "colt", "selena", "pablo"]
print(f"{name_list}")

name_list.reverse()
print(f"{name_list}")

# .sort() method = sorts the order of elements of the list in ascending order (in-place)
print("\nUsing .sort() method")
name_list = ["colt", "blue", "arya", "lena", "colt", "selena", "pablo"]
print(f"{name_list}")
name_list.sort()
print(f"{name_list}")

number_list = [6, 4, 1, 2, 5, 3]
print(f"{number_list}")
number_list.sort()
print(f"{number_list}")

# .join() method = a string method that takes a list & concatenates copy of the items into a new string
print("\nUsing .join() method")
word_list = ["Coding", "is", "fun"]
print(word_list)
string_from_list = ' '.join(word_list)
print(f"{string_from_list}")

name_list = ["Mr", "Bond"]
print(name_list)
string_from_list = '. '.join(name_list)
print(f"{string_from_list}")

friend_list = ["colt", "blue", "arya", "lena", "selena", "pablo"]
friend_string = ', '.join(friend_list)
print(f"I am friends with: {friend_string}.")
