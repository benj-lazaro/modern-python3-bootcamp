# special methods & inheritance demo
class GrumpyDict(dict):
    # NOTE: There is no ___init__() on this class since you're tapping dict's __init__() via MRO
    def __repr__(self):
        """__repr__(self) returns a string and dictionary item(s)."""
        print("None of your business.")
        return super().__repr__()       # Access dict's own __repr__() method


    def __missing__(self, key):
        """__missing__(self, key) returns a string if passed with an non-existent dictionary key."""
        print(f"You want {key}? Well, it ain't here.")


    def __setitem__(self, key, value):
        """__setitem__(self, key, value) assigns a new value to dictionary key & returns a string."""
        print("You want to change the contents of the dictionary?")
        print("Ok. Fine. Sigh!")
        super().__setitem__(key, value)


    def __contains__(self, item):
        """__contains__(self, item) checks if key is present w/in dict, returns a string and False regardless."""
        print("No, it ain't here.")
        return False


print("Instantiating sub-class GrumpyDict (of the Class Dict) into an object...")
data = GrumpyDict({
    "first": "Tom",
    "animal": "cat"
})

print("\nAccessing content of the instantiated dictionary object...")
print("Statement: data")
print(f"Result: {data}")

print("\nAccessing a non-existent dictionary key...")
print("Statement: data['city']")
data['city']

print("\nAdd a new key-value pair item to the instnatiated dictionary object...")
print("Statement: data['city'] = 'Tokyo'")
data["city"] = "Tokyo"

print("\nAccessing updated content of the instantiated dictionary object...")
print("Statement: data")
print(f"Result: {data}")

print("\nCheck if passed dict key is present within the dictionary...")
print("Statement: 'city' in data")
'city' in data
