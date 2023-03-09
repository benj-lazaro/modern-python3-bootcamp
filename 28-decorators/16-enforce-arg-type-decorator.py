# Enforcing argument value types with a decorator
def enforce(*arg_types):
    def decorator(func):
        def new_func(*args, **kwargs):
            # Convert argument values into something mutable since *args is NOT mutable
            new_args = []

            # Enforce passed  datatype (types) into each passed argument values (arg_value)
            for (arg_value, arg_type) in zip(args, arg_types):
                new_args.append(arg_type(arg_value))

            # Call passed function with contents of *new_args as replacement to *args
            return func(*new_args, **kwargs)
        return new_func
    return decorator


@enforce(str, int)              # Enforce 1at argument value to be str & 2nd argument value to be int
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)



@enforce(int, int)
def divide(num1, num2):
    print(num1 / num2)


# Test Code
repeat_msg("hello", '3')
repeat_msg("This is a test", 5)

divide(2, 2)
divide("10", "2")