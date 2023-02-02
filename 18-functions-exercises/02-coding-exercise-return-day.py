# Write a function called return_day
# Takes 1 parameter = a number from 1 to 7
# Returns the day of the week; 1 = Sunday
# If number i is less than 1 or greater than 7, return None

def return_day(number):
    """return_day(number) accepts an integer between 1 to 7 & returns the day of week (1 = Sunday, 2 = Monday, etc.)"""
    if number == 1:
        return "Sunday"
    elif number == 2:
        return "Monday"
    elif number == 3:
        return "Tuesday"
    elif number == 4:
        return "Wednesday"
    elif number == 5:
        return "Thursday"
    elif number == 6:
        return "Friday"
    elif number == 7:
        return "Saturday"
    return None

print("Function: return_day()")
print(f"Documentation: {return_day.__doc__}")
user_input = int(input("Enter number of day: "))
print(f"You have chosen: {return_day(user_input)}")
