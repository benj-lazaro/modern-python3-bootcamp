from random import randint

# Generate a random number between 1 and 10
# Until the random number == 5
# Every iteration, increment the value of the variable i

number = 0
i = 0

while number != 5:
    number = randint(1,10)
    print(f"Current random number is {number}")
    i += 1
