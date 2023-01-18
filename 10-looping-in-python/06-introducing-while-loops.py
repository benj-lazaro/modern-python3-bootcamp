# Basic syntax of a while loop
conditional_variable = True

while conditional_variable:
    print("Ran from within a while loop.")
    # To break from the while loop; preventing an infinite loop
    break

secret_password = str(input("What's the secret password: "))
while secret_password != "banana":
    print(f"{secret_password} is not the secret password. Please try again.")
    secret_password = str(input("What's the secret password: "))

print("Secret password accepted.")

# Looping through a series of number
print("Loop through 1 to 10:")
number = 1
while number < 11:
    print(number)
    number +=1
