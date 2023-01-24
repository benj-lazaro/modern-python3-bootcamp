# Create a new variable called answer
# It will contain a list of the 1st letter of each name from the list called names
names = ["Elie", "Tim", "Matt"]
answer = [name[0] for name in names]
print(names)
print(answer)

# Create a new variable called answer2
# It will contain a list of the 1st even numbers from the list numbers
numbers = [1, 2, 3, 4, 5, 6]
answer2 = [num for num in numbers if num % 2 == 0]
print(numbers)
print(answer2)
