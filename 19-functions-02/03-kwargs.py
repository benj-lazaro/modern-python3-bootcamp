# **kwargs (keyword args) = a special operator passed into a function as a parameter in the form of a dictionary
def fav_colors(**kwargs):
    """fav_colors(**kwargs) returns a string regarding a person's favorite color."""
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")


def special_greeting(**kwargs):
    """special_greeting(**kwargs) returns a special greeting to a specific name."""
    if "Bob" in kwargs and kwargs["Bob"] == "special":
        return "You get a special greeting Bob!"
    elif "Bob" in kwargs:
        return f"{kwargs['Bob']} Bob!"
    return "Not sure who is this..."


print("Function: fav_colors()")
print(f"Documentation: {fav_colors.__doc__}")
fav_colors(colt="royal deep amazing purple", ruby="red", ethel="teal")
fav_colors(ted="blue")
fav_colors(panther="pink", sasha="grey", bruce="black")

print("\nFunction: special_greeting()")
print(f"Documentation: {special_greeting.__doc__}")
print(special_greeting(Bob="Hello"))
print(special_greeting(Bob="special"))
print(special_greeting(David="Hi"))
print(special_greeting(Heather="Hey there", Bob="special"))
