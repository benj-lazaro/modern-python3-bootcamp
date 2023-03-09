# When we write
@decorator
def func(*args, **kwargs):
    pass

# We are actually doing this:
func = decorator(func)


# When we write
@decorator_with_args(arg)
def func(*args, **kwargs):
    pass

# We are actually doing this:
func = decorator_with_args(arg)(func)
