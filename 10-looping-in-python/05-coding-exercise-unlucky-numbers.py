# Loop though numbers 1 to 20
# For numbers 4 and 13, print "x is unlucky"
# For even numbers, print "x is even"
# For odd numbers, print "x is odd"

number_type = ""

for number in range(1, 21):
    if number == 4 or number == 13:
        number_type = "UNLUCKY"
    elif number % 2 == 0:
        number_type = "even"
    else:
        number_type = "odd"

    print(f"{number} is {number_type}")

