# Basic syntax of a list
tasks = ["Install Python", "Learn Python", "Take a break"]
print(tasks)

# List of variable items
first_task = "Install Python"
second_task = "Learn Python"
third_task = "Take a break"
task_list = [first_task, second_task, third_task]
print(task_list)

# List of different typed items
demo_list = ["a", 1, 45, True, 6.777]
print(demo_list)

# Use len() to determine the number of items in a list
print(len(demo_list))

# Use list() to convert an iterable using range() into a list
list_of_numbers = list(range(1, 10))
print(list_of_numbers)

# Convert a string into a list of characters
characters_of_a_string = list("this is a string")
print(characters_of_a_string)
