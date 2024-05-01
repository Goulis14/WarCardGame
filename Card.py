import main


class Card:
    def __init__(self, suits, ranks):
        self.suits = main.suits
        self.ranks = main.ranks
        self.value = main.values[ranks]

    def __str__(self):
        return self.ranks + " of " + self.suits

