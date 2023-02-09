# reversed = a way to reverse any iterator
# NOTE: returns a reversed iterator object

string_data = "hello world"
print(f"string_data: {string_data}")
print("Statement: ''.join(reversed(string_data))")
reversed_string = "".join(reversed(string_data))
print(f"Result: {reversed_string}")

print("\nUsing reversed() in a for loop with range():")
for number in reversed(range(0, 6)):
    print(number)
