import random
from Card import Card
suits= ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}

class Deck:
    '''
    Deck of cards (52 total)
    '''
    def __init__(self):
        '''
        Deck constructor
        '''
        self.all_cards = []

        for i in suits:
            for j in ranks:
                created_card = Card(i, j)
                self.all_cards.append(created_card)


    def shuffle(self):
        '''
        Shuffle Deck Method
        '''
        random.shuffle(self.all_cards)

    def deal_one(self):
        '''
        Deals one card from the deck
        '''
        return self.all_cards.pop()
    
    def add_one(self, card):
        self.all_cards.append(card)