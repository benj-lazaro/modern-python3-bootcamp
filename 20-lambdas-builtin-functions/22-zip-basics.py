# zip = accepts iterables (preferably of the same length)
# Returns an iterator of tuples where it pairs up the elements of both iterables
# Iterator stops when the shortest input iterable is exhausted

list_data_01 = [1, 2, 3, 4]
list_data_02 = [5, 6, 7, 8]
list_data_03 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
string_data = ['hi', 'lol', 'hahaha', ':-)']

print(f"list_data_01: {list_data_01}")
print(f"list_data_02: {list_data_02}")
print("Statement: zip(list_data_01, list_data_02)")
print(f"Result: {zip(list_data_01, list_data_02)}")

print("\nStatement: list(zip(list_data_01, list_data_02))")
print(f"Result: {list(zip(list_data_01, list_data_02))}")

print("\nStatement: list(zip(list_data_02, list_data_01))")
print(f"Result: {list(zip(list_data_02, list_data_01))}")

print("\nStatement: dict(zip(list_data_01, list_data_02))")
print(f"Result: {dict(zip(list_data_01, list_data_02))}")

print(f"\nlist_data_01: {list_data_01}")
print(f"list_data_03: {list_data_03}")
print("Statement: list(zip(list_data_01, list_data_03))")
print(f"Result: {list(zip(list_data_01, list_data_03))}")

print(f"\nlist_data_01: {list_data_01}")
print(f"string_data: {string_data}")
print("Statement: list(zip(list_data_01, string_data))")
print(f"Result: {list(zip(list_data_01, string_data))}")


# To unpack zipped iterable uzing zip()
zipped_data =   [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print("\nTo unpack a zipped iterable using zip(*<iterable>)")
print("---------------------------------------------------")
print(f"zipped_data: {zipped_data}")
print("Statement: list(zip(*zipped_data))")
print(f"Result: {list(zip(*zipped_data))}")
