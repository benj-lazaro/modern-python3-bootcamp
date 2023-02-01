# Write a function called speak
# It accepts a single parameter called animal
# Returns a corresponding string dependent on the arguement value
# If no argument value is passed, the value will default to "dog"
# If argument value is anything else, return a "?"

def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal =="dog":
        return "woof"
    else:
        return "?"

print(speak())
print(speak("cat"))
print(speak("banana"))
