

class Player:
    def __init__(self, name):
        self.name = name
        # A new player has no cards
        self.cards = []

    def remove_one_card(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.cards.pop(0)

    def add_card(self, newCard):
        if type(newCard) == type([]):
            self.cards.extend(newCard)
        else:
            self.cards.append(newCard)

    def __str__(self):
        return f"{self.name} has {len(self.cards)} cards"
