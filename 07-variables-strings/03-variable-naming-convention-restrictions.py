# Variable Naming Restrictions
# ============================

# Variable name must start with a letter or underscore
_cats = "Felix"
print(_cats)

# Rest of the name must consist of letters, numbers or underscores
cats2 = "Garfield"
print(cats2)

# Variable names are case-sensitive
CATS = "Snuggles"
print(CATS)
print(cats)     # Triggers a NameError since the variable cats is not defined


# Variable Naming Conventions
# ===========================

# Most variable names uses snake_case & lowercase
cat_name = "put-put"

# A constant variable name uses captal snake_case
PI_number = 3.1415

# A class name uses UpperCamelCase
class ClassName:
    pass

# A dunder variable starts and ends with two underscore characters
__no_touchy__

