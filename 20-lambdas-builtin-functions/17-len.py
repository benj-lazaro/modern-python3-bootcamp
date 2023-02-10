# len = returns the length (number of items as an integer) of an object
# argument may be a sequence (list, string, tuple, range) or collection (dictionary, set)

list_data = [1, 2, 3, 4]
set_data = (1, 2, 3, 4, 5)
string_data = "awesome"
range_data = range(0, 10)
dictionary_data = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(f"list_data: {list_data}")
print("Statement: len(list_data)")
print(f"Result: {len(list_data)}")

print(f"\nset_data: {set_data}")
print("Statement: len(set_data)")
print(f"Result: {len(set_data)}")

print(f"\nstring_data: {string_data}")
print("Statement: len(string_data)")
print(f"Result: {len(string_data)}")

print(f"\nrange_data: {range_data}")
print("Statement: len(range_data)")
print(f"Result: {len(range_data)}")

print(f"\ndictionary_data: {dictionary_data}")
print("Statement: len(dictionary_data)")
print(f"Result: {len(dictionary_data)}")

# Behind the scenes
print("\n*****************************")
print("***** Behind the scenes *****")
print("*****************************")
print("Calls the __len__() method of the passed argument sequence or collection")
print("\nStatement: list_data.__len__()")
print(f"Result: {list_data.__len__()}")

print("\nStatement: set_data.__len__()")
print(f"Result: {set_data.__len__()}")

print("\nStatement: string_data.__len__()")
print(f"Result: {string_data.__len__()}")

print("\nStatement: range_data.__len__()")
print(f"Result: {range_data.__len__()}")

print("\nStatement: dictionary_data.__len__()")
print(f"Result: {dictionary_data.__len__()}")
