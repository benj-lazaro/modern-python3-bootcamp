# Write code that classifies randomly selected food from a list as fruit, meat or yuck

# NO TOUCHING ============================================
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
# NO TOUCHING =============================================

# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print(food)     # For debugging purposes

if food == 'apple' or food == 'grape':
    print("fruit")
if food == 'bacon' or food == 'steak':
    print("meat")
if food == 'dirt' or food == 'worm':
    print("yuck")
# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
