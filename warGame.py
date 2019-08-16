# War Game
# Isaac Cheung

import random
from random import shuffle
import shuffleCards

# an implementation of a circular queue
class Queue:
    def __init__(self, capacity):
        self.size = capacity
        self.items = []
        self.head = 0
        self.tail = 0
        self.count = 0
    
    def __str__(self):
        queue = ']'
        item = self.head
        for index in range(self.count):
            queue += str(self.items[item]) + ', '
            item = (item + 1) % self.size
        return queue + ']'
    
    def enqueue(self, item):
        if self.count == self.size:
            raise Exception('Error: Queue is full')
        if len(self.items) < self.size:
            self.items.append(item)
        else:
            self.items[self.tail] = item
        
        self.count += 1
        self.tail = (self.tail + 1) % self.size
    
    def dequeue(self):
        if self.count == 0:
            raise Exception('Error: Queue is empty')
        item = self.items[self.head]
        self.items[self.head] = None
        self.count -= 1
        self.head=(self.head + 1) % self.size
        return item         
    
    def peek(self):
        if self.count == 0:
            raise Exception('Error: Queue is empty')
        return self.items[self.head]
    
    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.count == self.size
    
    def get_size(self):
        return self.count
    
    def get_capacity(self):
        return self.size
    
    def clear(self):
        self.items = []
        self.head = 0
        self.tail = 0
        self.count = 0   
        
class OnTable:
    
    def __init__(self):
        self.__cards = []
        self.__faceUp = [] 
        
    def place(self, player, card, hidden):
        
        if player == 1:
            self.__cards.insert(0, card)
            self.__faceUp.insert(0, hidden)
            
        elif player == 2:
            self.__cards.append(card)
            self.__faceUp.append(hidden)
            
    def cleanTable(self):
        cards = list(self.__cards)
        self.__cards = []
        self.__faceUp = []
        
        return cards
    
    def __str__(self):
        strExp = '['
        
        for index in range(len(self.__cards)):
            if self.__faceUp[index]:
                strExp = strExp + self.__cards[index]
            else:
                strExp = strExp +'XX'
            if index + 1 < len(self.__cards):
                strExp = strExp + ', '
        return strExp + ']'
            
def compare(item1,item2):
    
    # ranks sorted in order of largest to smallest, this is our "key"
    ranks = ['A','K','Q','J','0','9','8','7','6','5','4','3','2']
    
    item1_index = ranks.index(item1[0])
    item2_index = ranks.index(item2[0])
    
    # if item1 is larger than item2
    if item1_index < item2_index:
        return 1
    
    # if item1 is the same as item2
    elif item1_index == item2_index:
        return 0
    
    # if item1 is smaller than item2
    elif item1_index > item2_index:
        return -1
            
def main():
    
    should_shuffle = input('Shuffle deck before we begin? y/n: ') 
    if should_shuffle == 'y':
        shuffleCards.shuffleDeck()
    
    # accounts for the possibility that the file doesn't exist
    try:
        # prompt user for file to open
        #file_name = input('Input filename please: ')        # file_name = 'shuffledDeck.txt'
        
        file_name = 'shuffledDeck.txt'
        
        # open and read file
        deck_file = open(file_name, 'r')
        deck_data = deck_file.read()
        deck_list = deck_data.splitlines()
        deck_file.close()
        
        # makes sure deck is capitalized
        for index in range(len(deck_list)):
            deck_list[index] = deck_list[index].upper()

        # makes sure that the deck is valid
        # aka 52 unique cards and properly formatted

        suits=["D", "C", "H", "S"]
        ranks=["K","Q","J","A","2","3","4","5","6","7","8","9","0"]
        cards = []
        for rank in ranks:
            for suit in suits:
                cards.append(rank+suit)
                
        # checks if deck size is valid        
        if len(deck_list) != 52:
            raise Exception('The deck does not contain 52 cards')
        
        # checks if cards ar formatted properly
        for card in deck_list:
            if len(card) != 2:
                raise Exception('The card is not formatted correctly')
            elif card[0] not in ranks:
                raise Exception('The card is not formatted correctly')
            elif card[1] not in suits:
                raise Exception('The card is not formatted correctly')
            
        # checks to see if all the cards in the deck are unique
        for card in deck_list:
            # if the deck given is unique then u can each card 
            # exactly once from a complete deck, if u have to 
            # remove it more than once it's not unique
            try:
                cards.remove(card)
            except ValueError:
                raise Exception('The deck contains atleast one duplicate card')

    except FileNotFoundError:
        raise Exception('The file does not exist')
    
    except:
        raise Exception('Unknown error')

    
    player_hand = Queue(52)
    computer_hand = Queue(52)
    
    # deal cards to players
    order = random.randint(1,2)     # 50% chance it's 1, 50% chance it's 2
    if order == 1:
        for card in deck_list:
            if player_hand.get_size() <= computer_hand.get_size():
                player_hand.enqueue(card)
            else:
                computer_hand.enqueue(card)
    else:
        for card in deck_list:
            if computer_hand.get_size() <= player_hand.get_size():
                computer_hand.enqueue(card)
            else:
                player_hand.enqueue(card)        
    
    game_mode = 0
    mode_types = [1,2,3]
    while game_mode not in mode_types:
        try:
            game_mode = int(input('Would you like to play war with 1, 2 or 3 cards face down '))
        except:
            print('Invalid input, try again')
        
    
    endGame = False     
    
    cardsOnTable = OnTable()
    
    human_has_cards = True
    computer_has_cards = True
    
    while not endGame:
        
        # player 1's (human player) turn
        if not player_hand.is_empty():
            faceUp1 = player_hand.dequeue()
            cardsOnTable.place(1, faceUp1 , True)
        else:       # if the hand is empty player 1 loses
            human_has_cards = False
            endGame = True
            print('Player1 has run out of cards')
            table_cards = cardsOnTable.cleanTable()
            shuffle(table_cards)
            for card in table_cards:
                computer_hand.enqueue(card)            
        
        # player 2's (computer player) turn
        if not computer_hand.is_empty():
            faceUp2 = computer_hand.dequeue()
            cardsOnTable.place(2, faceUp2 , True)
        else:       # if the hand is empty player 2 loses
            computer_has_cards = False
            endGame = True
            print('Player2 has run out of cards')
            table_cards = cardsOnTable.cleanTable()
            shuffle(table_cards)
            for card in table_cards:
                player_hand.enqueue(card)
                
        # display the cards on table
        print(str(cardsOnTable))
        
        # pause
        print('Player1: %i cards'%player_hand.get_size())
        print('Player2: %i cards'%computer_hand.get_size())
        pause = input('Press the return key to continue.')
        
        # compare cards
        if computer_has_cards and human_has_cards:
            compare_value = compare(faceUp1, faceUp2)
            if compare_value == 1:
                # give all the cards on the table to player 1 and clear table
                table_cards = cardsOnTable.cleanTable()
                shuffle(table_cards)
                for card in table_cards:
                    player_hand.enqueue(card)
                    
            elif compare_value == -1:
                # give all the cards on the table to player 2 and clear table
                table_cards = cardsOnTable.cleanTable()
                shuffle(table_cards)
                for card in table_cards:
                    computer_hand.enqueue(card)
                    
            else:
                # player 1 puts n amount of cards on the table
                for card_index in range(game_mode):
                    if not player_hand.is_empty():
                        faceDown1 = player_hand.dequeue()
                        cardsOnTable.place(1, faceDown1 , False)
                    else:
                        human_has_cards = False
                        print('Player1 has run out of cards')
                
                # if player 1 ran out of cards previously player 2 gets everything
                if not human_has_cards:
                    table_cards = cardsOnTable.cleanTable()
                    shuffle(table_cards)
                    for card in table_cards:
                        computer_hand.enqueue(card)
                    endGame = True
                        
                # player 2 puts n amount of cards on the table
                for card_index in range(game_mode):
                    if not computer_hand.is_empty():
                        faceDown2 = computer_hand.dequeue()
                        cardsOnTable.place(2, faceDown2 , False)
                    else:
                        computer_has_cards = False            
                        print('Player2 has run out of cards')
                    
                # if player 2 ran out of cards previously player 1 gets everything
                if not computer_has_cards:
                    table_cards = cardsOnTable.cleanTable()
                    shuffle(table_cards)
                    for card in table_cards:
                        player_hand.enqueue(card)     
                    endGame = True
        else:
            endGame = True
    
    if player_hand.is_full():
        winner = 'Player1'
    else:
        winner = 'Player2'
    
    print('The winner of this game is %s'%winner)
    input('press any key to close')
    
main()
