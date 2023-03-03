# Decorator = a function that wraps other function & change / enhance their behavior
# Decorator is an example of High Order Function
# Have their own syntax using the @ (syntatic sugar)

# Define a Decorator as function without using syntatic sugar @
def be_polite(func):
    """be_polite(function) executes and returns the wrapper()."""
    def wrapper():
        """wrapper() prints a string and calls the function passed from be_polite() argument."""
        print("What a pleasure to meet you!")
        func()
        print("Have a great day!")
    return wrapper


def greet():
    """greet() simply prints a string."""
    print("My name is Haruna.")


def rage():
    """rage() simply prints a string."""
    print("Graahh!!!")


# Test Code
greet_message = be_polite(greet)
greet_message()

print("\n")

polite_rage = be_polite(rage)
polite_rage()
