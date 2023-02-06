##############################
# APS106 Winter 2022 - Lab 6 #
##############################

import random
from itertools import combinations

#####################################
# HELPER FUNCTIONS TO HELP PLAY THE
# GAME - NO NEED TO EDIT THESE
#####################################

def generate_deck():
    """
    (None) -> [[suit, number],[suit,number], ...]

    Create a standard deck of cards with which to play our game.
    Suits are: spades, clubs, diamonds, hearts
    Numbers are: 1 -13 where the numbers represent the following cards:
        1  - Ace
        11 - Jack
        12 - Queen
        13 - King
        2-10 - Number cards
    """

    deck = []
    suits = ['spades','clubs','diamonds','hearts']

    for suit in suits:
        for number in range(1,14):
            deck.append([suit,number])

    return deck

def shuffle(deck):
    """
    (list) -> list

    Produce a shuffled version of a deck of cards. This should shuffle a deck
    containing any positive number of cards.

    Note, this function should return a new list containing the shuffled deck
    and not directly reorder the elements in the input list. That is, the
    list contained in 'deck' should be unchanged after the function returns.
    """

    shuffled_deck = random.sample(deck,len(deck))

    return shuffled_deck

#############################
# PART 1 - Deal card
#############################

def deal_card(deck,hand):
    """
    (list,list) -> None

    Deal a card from the first element in the deck list and add it to the list
    representing the player's hand. Both list input parameters
    are nested lists with each element in the list being a two-element
    list representing a card.
    
    Note that this function returns nothing! It modifies the two lists that 
    are passed in as parameters in place.

    """
    # TODO your code here    
    
    hand.append (deck [0])
    deck.remove (deck [0])
    return 

#############################
# PART 2 - Score Hand
#############################

def score_hand(hand):
    """
    (list) -> int

    Calculate the cribbage score for a hand of five cards. The input parameter
    is a nested list of length 5 with each element being a two-element list
    representing a card. The first element for each card is a string defining
    the suit of the card and the second element is an int representing the 
    number of the card.
    """
    
    # TODO your code here
    points=0
    spade=0
    clubs=0
    diamonds=0
    heart=0
    numbers=[]
    total=0
    for cardindex in range(len(hand)):
        kind=hand [cardindex] [0]
        
# spades        
        if kind =="spades" :  
            spade+=1
        if kind =="hearts" :  
            heart+=1
        if kind =="clubs" :  
            clubs+=1
        if kind =="diamonds" :  
            diamonds+=1        
    if spade==5:
        points+=5
    elif spade==4:
        points+=4
# hearts        
    if heart==5:
        points+=5
    elif heart==4:
        points+=4

# clubs        
    if clubs==5:
        points+=5
    elif clubs==4:
        points+=4
    
#suit diamonds        
    if diamonds==5:
        points+=5
    elif diamonds==4:
        points+=4
    
#find pairs 

    for cardindex in range(len(hand)):
        number=hand [cardindex] [1]
        numbers.append (number)
    
    for i in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
        occurences = numbers.count (i)
        if occurences==2:
            points+=2
        elif occurences==3:
            points+=6
        elif occurences==4:
            points+=12   
   
    from itertools import combinations 
    lst = numbers
    combos_of_two = list(combinations(lst, 2)) 
    combos_of_three = list(combinations(lst, 3)) 
    combos_of_four = list(combinations(lst, 4)) 
    combos_of_five = list(combinations(lst, 5)) 
    continues=True
                
    if continues==True:
        for index in range(len(combos_of_five)) :
            combination=combos_of_five[index]
            combination=list(combination)
            combination.sort()
            first= combination [0]
            test=[first, first+1, first+2,first+3,first+4]
            if test == combination:
                points+=5
                continues=False

    if continues==True:
        for index in range(len(combos_of_four)) :
            combination=combos_of_four[index]
            combination=list(combination)
            combination.sort()
            first= combination [0]
            test=[first, first+1, first+2,first+3]
            if test == combination:
                points+=4
                continues=False  
    if continues==True:
        for index in range(len(combos_of_three)) :
            combination=combos_of_three[index]
            combination=list(combination)
            combination.sort()
            first= combination [0]
            test=[first, first+1, first+2]
            if test == combination:
                points+=3
    value=0
    total=0
    for x in range(len(combos_of_five)) :
        combination=combos_of_five[x]
        combination=list(combination)
        
        value=0
        for x in combination: 
            if x>=11:
                value+=10
            else:
                value+=x
        if value==15:
            points+=2 
    for x in range(len(combos_of_four)) :
        combination=combos_of_four[x]
        combination=list(combination)
        
        value=0
        for x in combination: 
            if x>=11:
                value+=10
            else:
                value+=x
        if value==15:
            points+=2 
    for x in range(len(combos_of_three)) :
        combination=combos_of_three[x]
        combination=list(combination)
        
        value=0
        for x in combination: 
            if x>=11:
                value+=10
            else:
                value+=x
        if value==15:
            points+=2 
           
    for x in range(len(combos_of_two)) :
        combination=combos_of_two[x]
        combination=list(combination)
        value=0
        for x in combination: 
    
            if x>=11:
                value+=10
            else:
                value+=x
        if value==15:
            points+=2
    return points

################################
# PART 3 - PLAY
################################

def play(shuffled_deck):
    """
    (list) -> [str, int, int]
    
    Function deals cards to players, computes player scores, and
    determines winner.
    
    Function retuns a three-element list where the first element is a string
    indicating the winner, the second element is an int specifying player\'s
    score, and the third element is an int specifying dealer\'s score.
    """
    player_hand = []
    dealer_hand = []

    # TODO complete the function
    for x in range (5):
        deal_card(shuffled_deck,player_hand)
        deal_card(shuffled_deck,dealer_hand)
    
    playerscore=score_hand(player_hand)
    dealerscore=score_hand(dealer_hand)
    statement=[]
    if dealerscore>=playerscore :
        statement.append ("dealer wins")
    else :
        statement.append ("player wins")
    statement.append (playerscore)
    statement.append (dealerscore)
    return statement
