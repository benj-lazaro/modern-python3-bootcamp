# any = returns True if ANY of the elements of an iterable is truthy; False if the iterable is empty

number_list = [0, 1, 2, 3]
print(f"number_list: {number_list}")
print("Statement: any(number_list)")
print(f"Result: {any(number_list)}")

print(f"\nnumber_list: {number_list}")
print("Statement: any([number for number in number_list if number > 2])")
print(f"Result: {any([number for number in number_list if number > 2])}")
print("Statement: any([number > 2 for number in number_list])")
print(f"Result: {any([number > 2 for number in number_list])}")

print(f"\nnumber_list: {number_list}")
print("Statement: any([number for number in number_list if number > 5])")
print(f"Result: {any([number for number in number_list if number > 5])}")
print("Statement: any([number > 5 for number in number_list])")
print(f"Result: {any([number > 5 for number in number_list])}")

number_list = [2, 4, 6, 8, 10, 11, 13]
print(f"\nnumber_list: {number_list}")
print("Statement: any([number % 2 == 0 for number in number_list])")
print(f"Result: {any([number % 2 == 0 for number in number_list])}")
