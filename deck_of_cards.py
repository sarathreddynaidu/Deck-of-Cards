# Specifications

# Card class
# Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
# Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
# Card 's __repr__  method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)

# Deck class
# Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
# Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
# Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
# Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the end of the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
# Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should raise a ValueError  with the message "Only full decks can be shuffled". shuffle should return the shuffled deck.
# Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck and return that single card.
# Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards.

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
        return iter(self.cards)

    # VERSION USING A GENERATOR FUNCTION 
    # (covered in the next video)
    # def __iter__(self):
    #     for card in self.cards:
    #         yield card

    def reset(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        return self

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        """
        Return a list of cards dealt
        """
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
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)
        return self

    def deal_card(self):
        """
        Returns a single Card
        """
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        """
        Returns a list of Cards
        """
        return self._deal(hand_size)

my_deck = Deck()
my_deck.shuffle()

for card in my_deck:
    print(card)
	
# Test Cases 

# card = d.deal_card()
# print(card)
# hand = d.deal_hand(50)
# card2 = d.deal_card()
# print(card2)
# print(d.cards)
# card2 = d.deal_card()
