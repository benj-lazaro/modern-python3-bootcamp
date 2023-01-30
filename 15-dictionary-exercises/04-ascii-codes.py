# Create a dictionary that maps ASCII keys to their corresponding letters
# Use dictionary comprehension and chr()
# Target capital letters from A to Z (65 to 90)
answer = {index: chr(index) for index in range(65, 91)}
print(f"Answer: {answer}")
