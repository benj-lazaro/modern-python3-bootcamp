# Write a program that determines on whether to call in sick or not baesd on the random values of variables

# NO TOUCHING ======================================
from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

# NO TOUCHING ======================================

calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

if actually_sick and sick_days > 0:
	calling_in_sick = True
elif kinda_sick and hate_your_job and sick_days > 0:
	calling_in_sick = True
else:
	calling_in_sick = False

# For debugging purposes only
print(f"Actually sick: {actually_sick}")
print(f"Kinda sick: {kinda_sick}")
print(f"Hate your job: {hate_your_job}")
print(f"Sick days: {sick_days}")
print(f"Calling in sick: {calling_in_sick}")

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
