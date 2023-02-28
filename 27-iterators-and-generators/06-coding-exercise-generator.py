# Write a function called week
# It returns a generator object that yields each day of the week startin with Monday & ending on Sunday
# After Sunday, the generator is exhausted and does NOT start over

def week():
    """week() yields a generator object containing days of the week."""
    days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for day in days_list:
        yield day


# Test Code
days = week()                           # Assign the yielded generator object to the variable called days
print(f"{next(days)}\n")                # Access the first value of the generator object (i.e. Monday)

for day in days:
    print(day)                          # Access the remaining values of the generator object
