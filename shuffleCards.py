# Creates a deck of 52 shuffles cards and stores in file shuffledDeck.txt
# each line of the file is a card. A card is 2 characters. the first is the rank, the second is the suit
# Suits are D, C, H, and S
# Ranks are: K, Q, J, A, 2, 3, 4, 5, 6, 7, 8, 9, 0
#
from random import shuffle

def shuffleDeck():
    suits=["D", "C", "H", "S"]
    ranks=["K","Q","J","A","2","3","4","5","6","7","8","9","0"]
    
    cards=[]
    
    for rank in ranks:
        for suit in suits:
            cards.append(rank+suit)
            
            
    shuffle(cards)
    try:
        cardFile= open("shuffledDeck.txt", "w")
        for card in cards:
            cardFile.write(card+"\n")
    except IOError as e:
        print ("I/O error({0}: {1}".format(e.errno, e.strerror))
    except:
        print ("Unexpected error")
    finally:
        cardFile.close()
    print ("The shuffled 52 card deck was saved in shuffledDeck.txt")