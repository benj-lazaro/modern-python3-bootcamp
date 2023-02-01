# Common return mistakes
def sum_odd_numbers(numbers):
    total = 0

    for number in numbers:
        if number % 2 != 0:
            total += number
        return total            # Due to intendation, the total is immediately returned & breaks the loop

print(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7]))


def is_odd_number(number):
    if number % 2 != 0:
        return True
    else:                       # The else branch is unneccesary
        return False

print(is_odd_number(4))
print(is_odd_number(45))

def is_odd_number_v2(number):
    if number % 2 != 0:         # NOT exactly a mistake...
        return True             # Returns True if the number is odd
    return False                # Otherwise, returns False

print(is_odd_number(4))
print(is_odd_number(45))