# Write a function called compact
# Accepts 1 parameter (list)
# Returns a list of values that are truthy only

def compact(list_data):
    """compact(list) returns a list of truthy values only."""
    return [item for item in list_data if item]


list_sample = [0, 1, 2, "", [], False, {}, None, "All done"]

print("Function: compact()")
print(f"Documentation: {compact.__doc__}")
print(f"list_sample: {list_sample}")
print(f"Result: {compact(list_sample)}")
