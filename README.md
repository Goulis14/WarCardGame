# War Card Game

This is a Python implementation of the classic card game War. War is a simple game played with a standard deck of 52 cards, originally known as "War of the Cards." The game is typically played by two players, but it can also be played by more. 

## Rules of the Game
1. The deck is divided evenly between the two players.
2. Each player draws one card from the top of their deck in each round.
3. The player with the higher-ranked card wins the round and takes both cards, placing them at the bottom of their deck.
4. If the ranks of the drawn cards are equal, a "war" occurs:
   - Each player places three cards face down and then draws a fourth card face up.
   - The player with the higher-ranked fourth card wins all the cards in the war.
5. The game continues until one player wins by obtaining all the cards or until a certain number of rounds have been played.

## How to Play
1. Run the program.
2. Enter the names of Player 1 and Player 2.
3. The deck is shuffled and divided evenly between the players.
4. Players take turns drawing cards from their decks.
5. If a war occurs, follow the rules mentioned above.
6. The game ends when one player has all the cards or after a predetermined number of rounds.

## Files
- **Card.py**: Defines the Card class representing individual playing cards.
- **Deck.py**: Defines the Deck class representing a deck of cards and includes methods for shuffling and dealing cards.
- **Player.py**: Defines the Player class representing a player in the game.

## Usage
```python
python main.py
