# Create a variable called answer
# For all nubmers between 1 and (including) 100
# Assign a new list containing numbers that are divisible by 12
answer =  [num for num in range(1, 101) if num % 12 == 0]
print(f"answer: {answer}")
