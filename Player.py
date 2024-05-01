import main


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def remove_one_card(self):
        return self.cards.pop(0)

    def add_card(self, newCard):
        if type(newCard) == type([]):
            self.cards.extend(newCard)
        else:
            self.cards.append(newCard)

    def __str__(self):
        return f"{self.name} has {len(self.cards)} cards"
