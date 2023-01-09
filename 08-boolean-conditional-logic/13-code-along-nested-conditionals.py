# Bounder pseudo code
# 1. Ask for age
# 2. Ages between 18 to 21 must have a wristband
# 3. Ages 21+ gets to drink alcohol and allow entry to concert(s)
# 4. Otherwise, categorized as 'too young'

age = input("How old are you? ")

if age:
    age = int(age)
    if age >= 21:
        print("You are good to enter and drink.")
    elif age >= 18:
        print("You can enter, but need a wristband.")
    else:
        print("You can't come in, little one. :(")
else:
    print("Please enter an age. ")

