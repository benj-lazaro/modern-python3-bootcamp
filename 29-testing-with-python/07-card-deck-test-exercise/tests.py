from card import Card
from deck import Deck
import unittest

class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "A")


    def test_init(self):
        """Cards should have a suit & a value."""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")


    def test_repr(self):
        """repr should return a string of the from 'Value of Suit'"""
        self.assertEqual(repr(self.card), "A of Hearts")


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()


    def test_init(self):
        """Decks should have a cards attribute"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)


    def test_repr(self):
        """repr should return a string 'Deck of 52 cards'"""
        self.assertEqual(repr(self.deck), "Deck of 52 cards.")


    def test_count(self):
        """count should return a count of the number of cards."""
        self.assertEqual(self.deck.count(), 52)     # Total of 52 cards
        self.deck.cards.pop()                       # Remove a card from the deck
        self.assertEqual(self.deck.count(), 51)


    def test_deal_sufficient_cards(self):
        """_deal should deal the number of cards specified."""
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)


    def test_deal_insufficient_cards(self):
        """_deal should deal the number of cards left in the deck."""
        cards = self.deck._deal(100)                # Intentionally ask to deal more than 52 cards
        self.assertEqual(len(cards), 52)            # Check if 52 cars have been dealt
        self.assertEqual(self.deck.count(), 0)      # Check if the deck is empty


    def test_deal_no_more_cards(self):
        """_deal should throw a ValueError if the deck is empty."""
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)


    def test_deal_card(self):
        """deal_card should deal a single card from the deck"""
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(card, dealt_card)
        self.assertEqual(self.deck.count(), 51)



    def test_deal_hand(self):
        """deal_hand should deal the number of cards passed"""
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)


    def test_shuffle_full_deck(self):
        """shuffle should shuffle the deck if the deck is full."""
        cards = self.deck.cards[:]                   # Copy the state of cards in a deck to the variable cards
        self.deck.shuffle()                          # Shuffle cards inside a deck
        self.assertNotEqual(cards, self.deck.cards)  # Arrangement of the cards shouldn't be identical
        self.assertEqual(self.deck.count(), 52)      # The no. of cards should remain 52 since it only got shuffled


    def test_shuffle_not_full_deck(self):
        """shuffle should throw a ValueError of the deck isn't """
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()


if __name__ == "__main__":
    unittest.main()
