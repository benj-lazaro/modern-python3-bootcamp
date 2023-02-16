# _name = a naming convention for a private class (can still be accessed if wanted to)
# __name = name mangling -> _<class_name>__<attribute_name> (e.g. _Person__name)
# __name__ = a dunder method called name.

class Person:
    def __init__(self):
        self.name = "Stark"
        self._secret = "Hi!"
        self.__message = "I like ube!"
        self.__lol = "Oh yeah! Really."


# Instantiate class Person() into an object saved into the variable dude
dude = Person()

# Access attribute name
print(dude.name)

# Access private attribute (by convention) _secret
print(dude._secret)

# Access name mangled attribute _Person__message
print(dude._Person__message)
print(dude._Person__lol)
