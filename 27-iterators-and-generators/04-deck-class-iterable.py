# Section 25 Deck of Card (DoC) Deck Class as an iterable
from random import shuffle

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:

    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    def __iter__(self):
        """__iter__(self) converts Instance Attribute cards an an iterable."""
        return iter(self.cards)

    def reset(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        return self

    def count(self):

        return len(self.cards)

    def _deal(self, num):
        """_deal(self, num) returns a list of cards dealt."""
        count = self.count()
        actual = min([num, count])  # make sure we don't try to over-deal

        if count == 0:
            raise ValueError("All cards have been dealt")

        if actual == 1:
            return [self.cards.pop()]

        cards = self.cards[-actual:]  # slice off the end
        self.cards = self.cards[:-actual]  # adjust cards

        return cards

    def shuffle(self):
        """def shuffle(self) returns a shuffled self.cards ONLY when it is a full deck."""
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)
        return self

    def deal_card(self):
        """deal_card(self) returns a single Card."""
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        """deal_hand(self, int) returns a list of Cards."""
        return self._deal(hand_size)


# Test Code
my_deck = Deck()
my_deck.shuffle()

# Iterate through the deck
for card in my_deck:
    print(card)
