import Card
import Deck
import Player

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# game logic

player1 = Player.Player(input("What is the name for Player1"))
player2 = Player.Player(input("What is the name for Player2"))

newDeck = Deck.Deck()
newDeck.shuffle()

for i in range(26):
    player1.add_card(newDeck.deal())
    player2.add_card(newDeck.deal())

gameOn = True
roundNum = 0

while gameOn:
    roundNum += 1
    print(f"Round {roundNum}")

    # Check to see if a player is out of cards:
    if len(player1.cards) == 0:
        print("Player 2 wins")
        break
    if len(player2.cards) == 0:
        print("Player 1 wins")
        break

    # start new round
    player1_cards = [player1.remove_one_card()]

    player2_cards = [player2.remove_one_card()]

    # war case
    atWar = True
    while atWar:
        if player1_cards[-1].value > player2_cards[-1].value:
            # player1 takes the cards
            print("Player 1 wins and takes the cards")
            player1.add_card(player1_cards)
            player1.add_card(player2_cards)
            atWar = False
        elif player1_cards[-1].value < player2_cards[-1].value:
            # player2 takes the cards
            print("Player 2 wins and takes the cards")
            player2.add_card(player2_cards)
            player2.add_card(player1_cards)
            atWar = False
        else:
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.

            # First check to see if player has enough cards

            # Check to see if a player is out of cards:

            print("War!!!")
            if len(player1.cards) < 5:
                print("Game over, player2 wins")
                gameOn = False
                break
            elif len(player2.cards) < 5:
                print("Game over, player1 wins")
                gameOn = False
                break
            else:
                # Otherwise, we're still at war, so we'll add the next cards
                for num in range(5):
                    player1_cards.append(player1.remove_one_card())
                    player2_cards.append(player2.remove_one_card())
