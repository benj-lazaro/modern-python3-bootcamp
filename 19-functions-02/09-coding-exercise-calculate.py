# Write a function called calculate
# Accepts a list of keyword arguments (**kwargs)
# * make_float = a boolean, returns a float if True otherwse an integer
# * operation = add / subtract / multiply / divide
# * first = an integer value
# * second = an integer value
# * message = a string value

def calculate(**kwargs):
    """calculate(**kwargs) accepts multiple arguments; returns corresponding math operaiton & string message."""
    print(f"Received argument values: {kwargs}")

    # Check math operation
    if kwargs["operation"] == "add":
        result = kwargs["first"] + kwargs["second"]
    elif kwargs["operation"] == "subtract":
        result = kwargs["first"] - kwargs["second"]
    elif kwargs["operation"] == "multiply":
        result = kwargs["first"] * kwargs["second"]
    elif kwargs["operation"] == "divide":
        result = kwargs["first"] / kwargs["second"]

    # Check if result will be float or integer
    if kwargs["make_float"] == True:
        result = float(result)
    else:
        result = int(result)

    # Check for custom message
    message_string = "message" in kwargs.keys()

    if message_string == True:
        message_string = kwargs["message"]
    else:
        message_string = "The result is"

    return message_string + " " + str(result) + "."


print("Function: calculate()")
print(f"Documentation: {calculate.__doc__}")
print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))
print(calculate(make_float=False, operation='multiply', message='The product is', first=5, second=15))