# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 17:33:14 2018

@author: bdavis
"""
debug = True

class DeckSystem():

    def __init__(self):
        self.hand = []
        self.deck = []
        self.discard = []
        self.playing = []
    
    def fill_deck(self, cards_to_add): #arg: a list of cards
        if debug: print(cards_to_add)
        for i in range(len(cards_to_add)): #put each card into deck
            self.deck.append( cards_to_add[i] )        
            
    def draw(self, num_to_draw = 1):
        for i in range(num_to_draw):
            drawn_card = self.deck.pop(0) #draw the top card on the deck
            self.hand.append(drawn_card) #add the drawn card to hand
        
    def print_info(self,show_hand = False, show_deck= False, show_discard = False):
        
        print('HAND (', len(self.hand), ')')
        if show_hand: print('\t',self.hand)
        print('DECK (', len(self.deck), ')')
        if show_deck: print('\t',self.deck)
        print('DISCARD (', len(self.discard), ')')
        if show_discard: print('\t',self.discard)
        

def main():
    testgame = DeckSystem()
    
    testcards = ['copper','copper','copper','copper','copper','copper','copper','estate','estate','estate']
    
    testgame.fill_deck(testcards)
    print()
    testgame.print_info(True, True)
    
main()
