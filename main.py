import Card
import Deck
import Player

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

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
        if player1_cards[-1] > player2_cards[-1]:
            # player1 takes the cards
            print("Player 1 wins and takes the cards")
            player1.add_card(player1_cards)
            player1.add_card(player2_cards)
            atWar = False
        elif player1_cards[-1] < player2_cards[-1]:
            # player2 takes the cards
            print("Player 2 wins and takes the cards")
            player2.add_card(player2_cards)
            player2.add_card(player1_cards)
            atWar = False
        else:
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
                for num in range(5):
                    player1_cards.append(player1.remove_one_card())
                    player2_cards.append(player2.remove_one_card())
