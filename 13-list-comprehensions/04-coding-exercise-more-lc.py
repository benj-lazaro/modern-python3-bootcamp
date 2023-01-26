# Create a variable called answer
# Assign a new list that is the intersection of the values of the lists [1, 2, 3, 4] and [3, 4, 5, 6]
# The output should be [3,  4]
answer = [num1 for num1 in [1, 2, 3, 4] if num1 in [3, 4, 5, 6]]
print(f"answer: {answer}")

# Create a variable called answer2
# Assign a new list with each item in reverse and lowercase
answer2 = [person[::-1].lower() for person in ["Elie", "Tim", "Matt"]]
print(f"answer2: {answer2}")
