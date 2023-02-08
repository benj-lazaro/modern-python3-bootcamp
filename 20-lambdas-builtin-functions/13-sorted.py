# sorted = returns a new sorted list from the items in an iterable (besides list)
# NOTE: source iterable untouched

number_list = [10, 4, 98, 34, 72, 1]
print(f"number_list: {number_list}")
print("Statement: sorted(number_list)")
print(f"Result: {sorted(number_list)}")
print("Statement: sorted(number_list, reverse=True)")
print(f"Result: {sorted(number_list, reverse=True)}")

number_tuple = (10, 4, 98, 34, 72, 1)
print(f"\nnumber_tuple: {number_tuple}")
print("Statement: sorted(number_tuple)")
print(sorted(number_tuple))
print("Statement: sorted(number_tuple, reverse=True)")
print(sorted(number_tuple, reverse=True))
