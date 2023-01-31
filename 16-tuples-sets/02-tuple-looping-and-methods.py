# Iterating through tuple items using a for loop
name_tuple = ("Colt", "Blue", "Rusty", "Lassie")
month_tuple = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December")
print(f"tuple: {name_tuple}")
print(f"tuple: {month_tuple}")

print("\nIterating through tuple values using a for loop:")
for name in name_tuple:
    print(name)

print("\nIterating through tuple values using a for loop:")
for month in month_tuple:
    print(month)


# Iterating through tuple values using a while loop
print("\nIterating through tuple items using a while loop:")
index = len(month_tuple) - 1

while index >= 0:
    print(month_tuple[index])
    index -= 1


# .count() = returns the number of times an value appears in a tuple
print("\nusing .count() method:")
number_tuple = (1, 2, 3, 3, 3)
print(f"tuple: {number_tuple}")

result = number_tuple.count(1)
print(f"Occurrence of 1 in the tuple: {result}")

result = number_tuple.count(2)
print(f"Occurrence of 2 in the tuple: {result}")

result = number_tuple.count(3)
print(f"Occurrence of 3 in the tuple: {result}")


# .index() = returns the index at which the 1st matching value is found in a tuple
print("\nusing .index() method:")
print(f"tuple: {number_tuple}")

result = number_tuple.index(3)
print(f"Index of the 1st matching value of 3 in tuple: {result}")
