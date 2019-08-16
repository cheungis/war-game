# war-game
A simulation of the card game "War".

The card game War is a card game that is played with a deck of 52 cards.
The goal is to be the first player to win all 52 cards. It is played by two 
players but can also be played with more.

The deck, after being shuffled, is divided evenly between the players. When 
there are two players each one receives 26 cards, dealt one at a time, face 
down. So the cards and their order are unknown. Each player places their stack
of cards face down. It may seem as a STACK as we know it, since the player takes
and plays one card at a time from the top of this stack. However, it is more 
like a QUEUE, since as we shall see it, when a player wins cards, these are 
placed at the bottom of this stack of cards.

Should run shuffleCards.py before starting the game to ensure the cards are shuffled.

The deck is stored in shuffledDeck.txt and is resistant to tampering since the file is validated by the game before the game starts.

Built using the Python language.
