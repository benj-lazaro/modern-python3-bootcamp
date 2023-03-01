# Write a function called yes_or_no
# Returns a generator that first yields yes then no, then yes then no and so on
def yes_or_no():
    """yes_or_no() returns a 'yes' first then a 'no' on the next; repeats the pattern on the next call."""
    answer = "yes"
    while True:
        yield answer
        if answer == "yes":
            answer = "no"
        else:
            answer = "yes"


# Test Code
test = yes_or_no()
print(next(test))
print(next(test))
print(next(test))
print(next(test))
