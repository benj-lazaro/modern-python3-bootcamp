# raise = helpful in creating your own exception / error message

def colorize(text, color):
    valid_color = ('red', 'blue', 'yellow', 'green', 'brown')

    if type(text) is not str:
        raise TypeError("value of parameter 'text' MUST be instance of str.")

    if type(color) is not str:
        raise TypeError("value of parameter 'color' MUST be instance of str.")

    if color not in valid_color:
        raise ValueError("value of parameter 'color' is invalid.")

    print(f"Printed '{text}' in color {color}.")


# Normal function invocation
colorize("hello", "red")

# Intentionally triggers a TypeError
# colorize(123, "red")
# colorize("hello", 456)

# Intentionally triggers a ValueError
# colorize("hello", "magenta")
