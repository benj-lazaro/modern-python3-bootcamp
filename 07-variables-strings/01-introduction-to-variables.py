# Variable assignment
print("Variable assignment")
x = 100
khaleesi_mother_of_dragons = 1
print(khaleesi_mother_of_dragons + x)

# Variable's value can be manipulated without changed
# As long as the result is not assigned back to the variable
print("Variable value manipulation")
num_of_cats = 99
print(num_of_cats)
print(num_of_cats * 2)          # Performs operation without replacing the value in the variable
print(num_of_cats)              # Retains the variable's original value
num_of_cats = num_of_cats - 1
print(num_of_cats)

# Variables assigned to another variable
print("Variables assigned to another variable")
python_is_awesome = 100
just_another_var = python_is_awesome
print(python_is_awesome)
print(just_another_var)

friends = 0
friends = num_of_cats
print(friends)

# Variables can be reassigned with another value at any time
print("Variable reassignment")
python_is_awesome = 1337
print(python_is_awesome)

# Values assigned to different variables in a single line of code
print("Variables assignment in a single line")
all, at, once = 5, 10, 15
print(all)
print(at)
print(once)
