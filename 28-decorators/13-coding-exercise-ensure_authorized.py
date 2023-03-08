# Write a function called ensure_authorized
# It accepts a function and returns another function
# The passed function should ONLY be invoked if there exists a keyword argument with
# the name of 'role' and value of 'admin'
# Otherwise, the inner function returns a string 'Unauthorized'
from functools import wraps


def ensure_authorized(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper(*args, **kwargs) returns the passed function if pre-defined keyword argument value is met."""
        if ('role', 'admin') in kwargs.items():
            return func(*args, **kwargs)
        return "Unauthorized"
    return wrapper


@ensure_authorized
def show_secrets(*args, **kwargs):
    """show_secrets(*args, **kwargs) returns a string."""
    return "Shh! Don't tell anyone."


print(show_secrets(role="admin"))
print(show_secrets(role="nobody"))
print(show_secrets(a="b"))
