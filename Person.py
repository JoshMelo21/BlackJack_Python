import random
from Deck import Deck
from Card import Card

class Person():

    def __init__(self):
        self.chips =5
        self.cards= []
    
    def getChips(self):
        return self.chips
    
    def addChips(self, toAdd):
        self.chips += toAdd

    def betChips(self, toRemove):
        notRemoved = True
        while notRemoved:
            if toRemove <= self.chips:
                self.chips = self.chips -toRemove
                return toRemove
            else:
                toRemove = int(input("You do not have enough chips for this. Your current chips are {}. Please enter a new value:".format(self.chips)))
    
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

deck = Deck()

player = Person()
pCards = []

computer = Person()
cCards = []
playerSum =0

game = True


while game:
    ace =''
    pCL = len(pCards)
    for i in range(pCL):
        c = pCards.pop()
        if c.value ==1:
            c.value==11
        deck.add_one(c)

    cCL = len(cCards)
    for i in range(cCL):
        c2= cCards.pop()
        if c2.value ==1:
           c2.value =11
        deck.add_one(c2)
    print("Shuffling deck.....")
    deck.shuffle()

    if player.getChips() == 0:
        print("You ran out of chips! Game over!")
        game = False
        break
    busted = False
    won = False
    playerSum=0
    compSum =0

    print("\nYour current chips are: {}".format(player.getChips()))
    bet = int(input("How many chips would you like to bet?\n"))
    bet =player.betChips(bet)

    print("Game Beginning\n")
    cCards.append(deck.deal_one())
    cCards.append(deck.deal_one())
    print("Dealers Cards: {} ?\n".format(cCards[0]))

    pCards.append(deck.deal_one())
    pCards.append(deck.deal_one())
    print("Your cards: " + " ".join(map(str,pCards)))
    if pCards[0].value ==11:
        ace = input("You drew an ace: Enter 'c' to change the value to 1. Enter anything else to keep 11:\n")
        if ace =='c':
            pCards[0].value=1
        print("Value set")
    if pCards[1].value ==11:
        ace = input("You drew an ace: Enter 'c' to change the value to 1. Enter anything else to keep 11:\n")
        if ace =='c':
            pCards[1].value=1
        print("Value set")
        
    hit ="hit"
    for i in pCards:
            playerSum = playerSum + i.value
    while hit == "hit":
        hit = input("Type 'hit' to hit and 'stay' to stay\n")
        if hit == "stay":
            break
        pCards.append(deck.deal_one())
        if pCards[-1].value ==11:
            ace = input("You drew an ace: Enter 'c' to change the value to 1. Enter anything else to keep 11:\n")
            if ace =='c':
                pCards[-1].value=1
            print("Value set")
        playerSum= playerSum + pCards[-1].value
        print("Your cards: " + " ".join(map(str,pCards)))
        if playerSum > 21:
            print("You busted with a total of: {}".format(playerSum))
            busted = True
            break
    if busted:
        continue
    for i in cCards:
        compSum = compSum + i.value
    print("Dealer Cards : " + " ".join(map(str,cCards)))
    if compSum>playerSum:
        print("Dealer wins!")
        continue
    while compSum<playerSum and compSum<17:
        cCards.append(deck.deal_one())
        print("Dealer Cards : " + " ".join(map(str,cCards)))
        compSum += cCards[-1].value

        if compSum >21:
            temp= len(cCards)
            count =0
            while compSum>21 and count<temp:
                if cCards[count].value ==11:
                   cCards[count].value =1
                   compSum = compSum -10
                count+=1


        if compSum >21:
            print("Dealer busted with sum {} you won! You won {} chips".format(compSum,bet*2))
            player.addChips(bet*2)
            won = True
            break
    if compSum>playerSum and (not won):
        print("Dealer Won with : " + " ".join(map(str,cCards)) +" and a value of {}".format(compSum))
    elif compSum ==playerSum:
        print("Draw. Your chips were returned. Your total: {} Dealer total: {}". format(playerSum, compSum))
        player.addChips(bet)
    else:
        print("You won {} chips".format(bet*2))
        player.addChips(bet*2)