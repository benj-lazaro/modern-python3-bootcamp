# Assertions / assert statement (not a function)
# It allows to assert an expression that MUST be True (using the keyword assert)
# Otherwise, it throws an AssertionError
# The keyword assert accepts an expression
# It returns None if the expression is truthy
# It raises an AssertionError if the expression is falsy
# It accepts an optional error message as 2nd argument
# NOTE: assert statement(s) wiil NOT be evaluated when the code is run in optimized mode (-O flag)


def add_positive_numbers(first_number, second_number):
    """add_positive_numbers(positive number, positive number) test passed argument values & returns the sum."""
    assert first_number > 0 and second_number > 0, "Both numbers MUST be positive."
    return first_number + second_number


def eat_junk(food):
    """eat_junk(str) test passed argument value & returns a string."""
    assert food in ["pizza", "ice cream", "candy", "fried butter"], "food must be a junk food."
    return f"Nom Nom Nom, I'm eating {food}."


# Test Code
print(add_positive_numbers(1, 1))
print(add_positive_numbers(2.2, 1))
# print(add_positive_numbers(1, -1))  # Triggers an AssertionError with custom error message

chosen_food = str(input("Enter your preferred junk food: "))
print(eat_junk(chosen_food))
