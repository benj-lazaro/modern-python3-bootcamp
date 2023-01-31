# Basic syntax of a set
# {<value_1>, <value_2>, <value_n>}    = immutable data structure

# Set = a collection of data that DO NOT contain duplicate values & are NOT ordered
#     = duplicate values are reduced to a single copy
#     = values can NOT be accessed using an index but can iterated through using a loop

number_set = {1, 2, 3, 4, 5}
print(f"number_set: {number_set}")

# To confirm the existence of a value in the number_set
print("\nTo confirm existence of the value '4' in the number_set:")
result = 4 in number_set
print(f"Result: {result}")

print("\nTo create a new set using set():")
new_number_set = set({1, 4, 5})
print(f"new_number_set: {new_number_set}")


# Iterating through set values using a for loop
print("\nIterating through set values using a for loop:")
print(number_set)
for number in number_set:
    print(number)

# Set use case
print("\nSet use-case:")
cities = ["Los Angeles", "Boulder", "Kyoto", "Florence", "Santiago", "Los Angeles", "Shanghai", "Boulder",
          "San Francisco", "Oslo", "Tokyo"]
print(f"List of cities: {cities}")

print("\nEliminate list item duplicates using set(): ")
cities_unique = set(cities)
print(f"Result: {cities_unique}")

print("\nNumber of unique cities using len():")
cities_unique_number = len(cities_unique)
print(f"Result: {cities_unique_number}")

print("\nConvert set back into a list using list():")
result = list(cities)
print(f"Result: {result}")
