# Logical and & or demo

age = int(input("What is your age? "))

if age > 2 and age < 8:
    print("You will pay the child price.")

city = str(input("Where do you live? "))

if city == "los angeles" or city == "san francisco":
    print("You live in California!")
else:
    print("You live somewhere else.")
