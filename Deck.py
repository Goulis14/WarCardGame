import random
import main
from Card import Card


class Deck:
    def __init__(self):
        self.cards = []
        for suit in main.suits:
            for rank in main.ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
