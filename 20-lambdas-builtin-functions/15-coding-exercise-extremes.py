# Write a function called extremes
# Accepts an iterable
# Returns a tuple comtaining minimum and maximum elements

def extremes(iterable):
    """extremes(iterable) accepts an iterable and returns a tuple containing both minimum & maximum elements."""
    return (min(iterable), max(iterable))


test_data_01 = [1, 2, 3, 4, 5]
test_data_02 = [99, 25, 30, 7]
test_data_03 = "alcatraz"

print("Function: extremes()")
print(f"Documentation: {extremes.__doc__}")
print(f"test_data_01: {test_data_01}")
print("Statement: extremes(test_data_01)")
print(f"Result: {extremes(test_data_01)}")

print(f"\ntest_data_02: {test_data_02}")
print("Statement: extremes(test_data_02)")
print(f"Result: {extremes(test_data_02)}")

print(f"\ntest_data_03: {test_data_03}")
print("Statement: extremes(test_data_03)")
print(f"Result: {extremes(test_data_03)}")
