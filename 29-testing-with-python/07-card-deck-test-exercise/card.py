# Implement a class called Card
# Each instance should have an attribute called suit (Hearts, Diamonds, Clubs or Spades)
# Each instance should have an attribute called value (2 to 10, A, K, Q, or J)
# The __repr__() should display the card's value and suit (e.g. A of Hearts)
class Card:
    def __init__(self, suit, value):
        # Instance Attribute(s)
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"
