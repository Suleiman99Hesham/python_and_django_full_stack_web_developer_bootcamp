#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        print("Creating New Ordered Deck")
        self.cards = [(i,k) for i in SUITE for k in RANKS]

    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.cards)

    def split(self):
        return(self.cards[:26], self.cards[26:])

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards_in_hand = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards_in_hand))

    def add_cards(self,added_card):
        self.cards_in_hand.extend(added_card)

    def remove_card(self):
        return self.cards_in_hand.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__ (self,name,hand):
        self.name = name
        self.hand = hand
    
    def play_card(self):
        played_card = self.hand.remove_card()
        print("{} has played {}\n".format(self.name,played_card))
        return played_card

    def remove_war_cards(self):
        war_cards=[]
        if len(self.hand.cards_in_hand) >= 2 :
            for x in range(3):
                war_cards.append(self.hand.remove_card())
        return war_cards

    def has_cards(self):
        """
        Returns True if player still has cards
        """
        return len(self.hand.cards_in_hand) > 0 

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# create the deck and split it into two halfs
dick=Deck()
dick.shuffle()
half_1, half_2 = dick.split()

#creating two instances from Player, one for COMP and one for the user of game
comp = Player("Computer",Hand(half_1))
name = input("Please enter your name: ")
user = Player(name, Hand(half_2))

# Set Round Count
total_rounds = 0
war_count = 0
# Let's play
while user.has_cards() and comp.has_cards():
    total_rounds += 1
    print("It is time for a new round!")
    print("Here are the current standings: ")
    print(user.name+" count: "+str(len(user.hand.cards_in_hand)))
    print(comp.name+" count: "+str(len(comp.hand.cards_in_hand)))
    print("Both players play a card!")
    print('\n')

    # Cards on Table represented by list
    table_cards = []

    # Play cards
    c_card = comp.play_card()
    p_card = user.play_card()

    # Add to table_cards
    table_cards.append(c_card)
    table_cards.append(p_card)

    # Check for War!
    if c_card[1] == p_card[1]:
        war_count +=1
        print("We have a match, time for war!")
        print("Each player removes 3 cards 'face down' and then one card face up")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        # Play cards
        c_card = comp.play_card()
        p_card = user.play_card()

        # Add to table_cards
        table_cards.append(c_card)
        table_cards.append(p_card)

        # Check to see who had higher rank
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add_cards(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add_cards(table_cards)

    else:
        # Check to see who had higher rank
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add_cards(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add_cards(table_cards)

print("Great Game, it lasted: "+str(total_rounds))
print("A war occured "+str(war_count)+" times.")
