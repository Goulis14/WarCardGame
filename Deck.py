import main
import Card
import random


class Deck:
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.cards = []
        for suit in main.suits:
            for rank in main.ranks:
                # This assumes the Card class has already been defined!
                self.cards.append(Card.Card(suit, rank))

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.cards)

    def deal(self):
        # Note we remove one card from the list of cards
        return self.cards.pop()
