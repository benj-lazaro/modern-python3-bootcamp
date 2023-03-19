# JSON pickling demo
# json.dumps() formats a Python object as a string of JSON; it returns a string
# After pickling:
# - data type None changed into null
# - tuple converted changed into list
# - double quotes changed into single quotes

import json


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


street_cat = Cat("Charles", "Tabby")                                # Instantiate class into an object
json_convert = json.dumps(street_cat.__dict__)                      # Save object in json format
print(json_convert)

json_convert = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])  # Save object in json format
print(json_convert)
