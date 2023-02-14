# __name__ = every python file, module has it's own __name__ variable
# the main file being run has the value of the variable __name__ = "__main__"

# *** This is the main file ***

# import 'revisited'
# 1. Python 1st finds the imported module, throws an error if it fails
# 2. Python runs the code inside the module being imported

from say_sup import say_sup
def say_hi():
    """say_hi() prints a string and the value of __name__."""
    print(f"Hi! My __name__ is {__name__}")


say_hi()
say_sup()