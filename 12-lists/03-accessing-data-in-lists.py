# Accessing values in a list
colors = ["Purple", "Teal", "Orange"]

# Starting index starts at 0
print("Colors from colors list")
print(colors[0])
print(colors[1])
print(colors[2])

# Negative index to access items backwards
print("\nAccessing list items backwards using negative index values")
print(colors[-1])
print(colors[-2])
print(colors[-3])

# Use "in" to check if an item exists inside a list
if "Teal" in colors:
    print("\nTeal exists in list")
    print("You have good taste in colors.")

