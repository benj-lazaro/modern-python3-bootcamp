# Basic try-except block

def get_dict_value(dict_data, key):
    """get_dict_value(dict, key) returns the corresponding value of the passed dictionary key."""
    try:
        return dict_data[key]
    except KeyError:
        return None


dictionary_sample = {
    "name": "Ricky"
}


print("Function get_dict_value():")
print(f"Documentation: {get_dict_value.__doc__}")
print(f"dictionary_sample: {dictionary_sample}")

print(f"\nStatement: get_dict_value(dictionary_sample, 'name')")
print(f"Result: {get_dict_value(dictionary_sample, 'name')}")

print(f"\nStatement: get_dict_value(dictionary_sample, 'city')")
print(f"Result: {get_dict_value(dictionary_sample, 'city')}")       # Accessing a non-existent dictionary key

print(f"\nStatement: get_dict_value(dictionary_sample, 'timezone')")
print(f"Result: {get_dict_value(dictionary_sample, 'timezone')}")   # Accessing a non-existent dictionary key
