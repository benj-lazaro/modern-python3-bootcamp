# jsonpickle demo
# This method is flexible compared to json pickling
# Easily read by another programming language (w/o any data conversions) as a json file with less line of code

import jsonpickle


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


# Instantiate class into an object
street_cat = Cat("Charles", "Tabby")

# Encode Python object into a jsonpickle and write it into a file
with open("cat.json", "w") as data:
    frozen_data = jsonpickle.encode(street_cat)
    data.write(frozen_data)

# Read from jsonpickle file
with open("cat.json", "r") as data:
    content = data.read()
    unfrozen_data = jsonpickle.decode(content)
    print(unfrozen_data)
