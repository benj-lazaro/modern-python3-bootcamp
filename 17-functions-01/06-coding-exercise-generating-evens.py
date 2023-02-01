# Write a function called generate_evens
# It returns a list of even numbers between 1 and (exclusive) 50
# Use either a for loop or List Comprehension

def generate_evens():
    return [number for number in range(1, 50) if number % 2 == 0]

print(generate_evens())
