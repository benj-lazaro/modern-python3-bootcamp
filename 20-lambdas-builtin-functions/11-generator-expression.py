import sys
# generator expression = lighter version of a list
# Use case: when iterating once & will NOT store the generated result

people_list = ["Charlie", "Casey", "Cody", "Carly", "Christina"]
print(f"people_list: {people_list}")
print("Statement: (name[0] == 'C' for name in people_list)")
print(f"Result: {(name[0] == 'C' for name in people_list)}")
print("Statement: any((name[0] == 'C' for name in people_list))")
print(f"Result: {any((name[0] == 'C' for name in people_list))}")
print("Statement: all((name[0] == 'C' for name in people_list))")
print(f"Result: {all((name[0] == 'C' for name in people_list))}")

# Genrator expression VS List comprehension
list_comprehension = sys.getsizeof([number * 10 for number in range(1000)])
generator_expression = sys.getsizeof(number * 10 for number in range(1000))

print("\nGenerator expression VS List comprehension")
print("Task: number * 10 for number in range(1000)")
print(f"List comprehension object size: {list_comprehension} bytes")
print(f"Generator expression object size: {generator_expression} bytes")
