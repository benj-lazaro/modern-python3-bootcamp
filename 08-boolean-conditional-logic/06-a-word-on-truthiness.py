# A demo on truthy and falsy (e.g. empty objects, strings, None & 0) values

if 0:
    print("Nay!")   # Line does not get executed due to falsy conditional value

if 1:
    print("Yay!")   # Line does get executed due to truthy conditional value

favorite_animal = str(input("What is your favorite animal? "))

if favorite_animal:
    print(f"Hey {favorite_animal} is my favorite too!")
else:
    print("You didn't say anything!")
