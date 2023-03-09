# Writing an ensure_first_arg_is a decorator
# Decorators that takes an argument value

from functools import wraps

def ensure_first_arg_is(arg_value):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] != arg_value:
                return f"First argument needs to be {arg_value}."
            return func(*args, **kwargs)
        return wrapper
    return inner


@ensure_first_arg_is("burrito")
def favorite_foods(*foods):
    # print(foods)
    return foods


@ensure_first_arg_is(10)
def add_to_ten(first_number, second_number):
    return first_number + second_number


# Test Code
print(favorite_foods("burrito", "ice cream"))
print(favorite_foods("burrito", "steak"))
print(favorite_foods("steak", "potatoes"))

print("\n")
print(add_to_ten(10, 10))
print(add_to_ten(1, 1))
