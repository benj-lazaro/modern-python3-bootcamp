from random import shuffle

class Card:
    def __init__(self, value, suit):
        # Instance Attribute(s)
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.suit} of {self.value}"


# Test code
my_card = Card("A", "Hearts")
print(my_card)
