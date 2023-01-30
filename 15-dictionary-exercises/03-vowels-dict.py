# Create a dictionary with keys as vowels and the value as 0
# Using dict()
print("Using dict():")
vowels = [['a',0],['e',0],['i',0],['o',0],['u',0]]
answer1 = dict(vowels)
print(f"Amswer: {answer1}")

# Using dictionary comprehension
print("\nUsing Dictionary comprehension:")
answer2 = {vowels[index][0]: vowels[index][1] for index in range(0, len(vowels))}
print(f"Answer: {answer2}")
