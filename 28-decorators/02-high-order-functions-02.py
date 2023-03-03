# High Order Function
# Nesting a function within another function demo

from random import choice

def greet(person):
    """greet(string) returns a string combined with the returned string from get_mood()."""

    def get_mood():
        """get_mood() returns a randomly selected greeting string."""
        message = choice(("Hello there ", "Go away ", "I love you "))
        return message

    result = get_mood() + person
    return result


def make_laugh_func():
    """make_laugh_func() returns the entire nested function get_lauch()."""
    def get_laugh():
        """get_laugh() returns a randonly selected laugh string."""
        laugh_string = choice(("Hahaha", "Lol", "Tee he he"))
        return laugh_string

    return get_laugh    # () removed so as to prevent getting executed immediately


def make_laugh_at_func(person):
    """make_laugh_at_func(string) returns the entire nested function get_lauch()."""
    def get_laugh():
        """get_laugh() returns a randonly selected laugh string with the argument value of person."""
        laugh_string = choice(("Hahaha", "Lol", "Tee he he"))
        return f"{laugh_string} {person}"

    return get_laugh


# Test Code
print("Calling greet()...")
message_greet = greet("Haruna")
print(f"Result: {message_greet}")

print("\nCalling make_laugh_func()...")
laugh = make_laugh_func()
print(f"Result: {laugh()}")

print("\nCalling make_laugh_at_func()...")
laugh_at = make_laugh_at_func("Sayumi")
print(f"Result: {laugh_at()}")
