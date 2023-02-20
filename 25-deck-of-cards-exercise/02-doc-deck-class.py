from random import shuffle

# Implement a class called Card
# Each instance should have a suit (Hearts, Diamonds, Clubs & Spades)
# Each instance should have a value (2 to 10, A, K, Q, & J)
# The __repr__() should display the card's value and suit (e.g. A of Hearts)

class Card:
    def __init__(self, value, suit):
        # Instance Attribute(s)
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


# Implement a class called Deck
# Each instance should have an attribute cards with all 52 instances of the Card class
# An instance method count() that returns how many cards remaining in the deck
# The __repr__() should display how many cards left in the deck
# An instance method _deal() w/c accepts a number and removes that many cards from the deck
# An instance method shuffle w/c ONLY shuffles a full deck of 52 cards
# An instance method deal_card w/c uses _deal() to deal/remove a single card from the deck
# An instance method deal_hand w/c accept a number to a deal a list of cards from the deck

class Deck:
    def __init__(self):
        # Instance Attribute(s)
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for value in values for suit in suits]

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    # Instance Method(s)
    def count(self):
        """count(self) returns the number of cards remaining in the deck."""
        return len(self.cards)

    def _deal(self, number_of_cards):
        """_deal(self, number_of_cards) removes the number of cards from the deck."""
        current_cards_in_deck = self.count()
        actual_cards_to_deal = min(current_cards_in_deck, number_of_cards)

        # If deck is empty, raise an error message
        if current_cards_in_deck == 0:
            raise ValueError("All cards have been dealt.")

        # Slice the cards beginning at the end of self.cards up to the specified number of cards to be dealt
        cards_taken_from_deck = self.cards[-actual_cards_to_deal:]

        # Update the deck by assigning the beginning of self.cards up to the index of the dealt card(s)
        self.cards = self.cards[:-actual_cards_to_deal]

        return cards_taken_from_deck

    def deal_card(self):
        """deal_card(self) removes 1 card (as value, not as a list item) from the deck."""
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        """deal_hand(self, hand_size) removes a number of cards from the deck."""
        return self._deal(hand_size)

    def shuffle(self):
        """shuffle(self) shuffles a full deck of cards (52 cards) ONLY."""
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled.")

        shuffle(self.cards)
        return self


# Test code
my_deck = Deck()
print(my_deck.cards)
# print(f"There are currently {my_deck.count()} card(s) in the deck.")
# print("Deal a card from the deck...")
# print(my_deck._deal(1))
# print(f"There are currently {my_deck.count()} card(s) in the deck.")
# print(my_deck)
# print("Deal 3 cards from the deck...")
# print(my_deck._deal(3))
my_deck.shuffle()
print(my_deck.cards)
print("Deal 10 cards from the deck...")
my_hand = my_deck.deal_hand(10)
print(my_hand)
print("Deal 1 card from the deck...")
my_card = my_deck.deal_card()
print(my_card)
print("Check deck size...")
print(my_deck)
