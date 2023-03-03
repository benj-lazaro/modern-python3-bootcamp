# Define a Decorator using syntactic sugar @

def be_polite(func):
    """be_polite(function) executes and returns the wrapper()."""
    def wrapper():
        """wrapper() prints a string and calls the function passed from be_polite() argument."""
        print("What a pleasure to meet you!")
        func()
        print("Have a great day!")
    return wrapper

@be_polite
def greet():
    """greet() simply prints a string."""
    print("My name is Haruna.")


@be_polite
def rage():
    """rage() simply prints a string."""
    print("Graahh!!!")


# Test Code
greet()
print("\n")
rage()
