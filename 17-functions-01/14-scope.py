# Scope = where variables can be accessed
# * Variables created in function are scaped in that function

# Global-scoped variable
instructor_global = "Colt"

def say_hello():
    # Local-scoped variable
    instructor_local = "Steele"

    return f"Hello {instructor_local}"

print("Invoking say_hello() function")
print(say_hello())
print(f"Accessing global variable: {instructor_global}")
# print(f"Accessing local variable: {instructor_local}")  # Triggers a NameError; unable to access variable


# Manipulating the value of a global variable
total = 0           # Global-scoped variable

def increment():
    global total    # NEED to declare global variable in order to use & manipulate value w/in a function
    total += 1      # UnboundLocalError if global variable in not declared within the function
    return total

print(f"\nIncrement function: {increment()}")


# Accessing value of a global variable
name = "Rusty"
def greet():
    return f"\nHi there, I'm {name}"  # NO need to use global keyword when access global variable values ONLY

print(greet())



# Keyword nonlocal = modify a parent's variables in a child (i.e. nested) function
def outer():
    count = 0               # Local variable
    def inner():
        nonlocal count      # Access the local variable count of outer()
        count += 1
        return count        # Returns incremented value back to outer()
    return inner()          # Returns the returned value of inner() to main

print(f"outer: {outer()}")
