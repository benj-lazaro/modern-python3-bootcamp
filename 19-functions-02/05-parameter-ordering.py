# Specific order of parameters
# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs           = collects the remaining argument values passed into the function

def display_info(a, b, *args, instructor="Colt", **kwargs):
    """display_info() accepts different parameters types & returns a list of passed argument values"""
    return [a, b, args, instructor, kwargs]


print("Function: display_info():")
print(f"Documentation: {display_info.__doc__}")
print(display_info(1, 2, 3, last_name="Steele", job="instructor"))
