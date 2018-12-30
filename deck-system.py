# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 17:33:14 2018

@author: edavis
"""
import random
debug = True


class DeckSystem():

    def __init__(self, deck_list):
        #top of pile always is index = 0
        self.hand = []
        self.deck = []
        self.discard = [] 
        self.playing = []
        
        self.turns_played = 0
        
        self.fill_deck(deck_list)
        self.shuffle_deck()
        if debug: print('DECK CREATED\nDeck:', self.deck)
    
    def fill_deck(self, cards_to_add): #arg: a list of cards
        #if debug: print(cards_to_add)
        for i in range(len(cards_to_add)): #put each card into deck
            self.deck.append( cards_to_add[i] )        
            
        if debug: print('FILLED DECK with cards:', cards_to_add)
            
    def draw(self, num_to_draw = 1):
        for i in range(num_to_draw):
            drawn_card = self.deck.pop(0) #draw the top card on the deck
            self.hand.append(drawn_card) #add the drawn card to the end (-1) of the hand
            
        if debug:print('DREW', num_to_draw, 'cards')
        
    def play_card(self, card_index):
        played_card = self.hand.pop(card_index) #get the card
        self.playing.append(played_card) #transfer the card to the end of the playing "deck"
        if debug: print('PLAYED', played_card, 'from hand')
        return played_card #to alert the other programs that the card was played
    
    def discard_cards(self, location = 'hand', card_index = 'all'):
        
        if card_index == 'all':
            #discard all of your hand or playing cards
            if location == 'hand':
                for i in range(len(self.hand)):
                    card = self.hand.pop(-1)
                    self.discard.insert(0, card)
                    
            elif location == 'playing':
                for i in range(len(self.playing)):
                    card = self.playing.pop(-1)
                    self.discard.insert(0, card)
                    
        else:
            #discard a specific card
            if location == 'hand':
                card = self.hand.pop( card_index)
                self.discard.insert(0, card)
                    
            if location == 'playing':
                card = self.playing.pop( card_index)
                self.discard.insert(0, card)
                    
        if debug: print('DISCARDED', card_index, 'from', location)       
        
    
    def gain_card(self, card, location = 'playing', top = True):
        if top == True:
            index_num = 0
        else: index_num = -1
        
        if location == 'playing':
            self.playing.insert(index_num, card)
        if location == 'hand':
            self.hand.insert(index_num, card)
        if location == 'discard':
            self.discard.insert(index_num, card)
        if location == 'deck':
            self.deck.insert(index_num, card)
        
        if debug:print('GAINED a', card, 'card (on top: ', top, ')')
                         
    
    def shuffle_deck(self, pile_to_shuffle = 'deck'):
        if pile_to_shuffle == 'deck':
            random.shuffle(self.deck)    
            
        elif pile_to_shuffle == 'discard': 
            #shuffle the discard and then put it under the deck
            random.shuffle(self.discard)
            for i in range(len(self.discard)):
                card = self.discard.pop()
                self.deck.append(card)
            
        elif pile_to_shuffle == 'both' or pile_to_shuffle == 'discard+deck': 
            #shuffle the deck and discard together
            for i in range(len(self.discard)):
                card = self.discard.pop()
                self.deck.append(card)
            random.shuffle(self.deck)
            
        elif pile_to_shuffle == 'all' or pile_to_shuffle == 'everything':
            #reshuffles everything together
            for i in range(len(self.discard)):
                card = self.discard.pop()
                self.deck.append(card)
            for i in range(len(self.playing)):
                card = self.playing.pop()
                self.deck.append(card)
            for i in range(len(self.hand)):
                card = self.hand.pop()
                self.deck.append(card)
                
            random.shuffle(self.deck)
            
        if debug: print('SHUFFLED', pile_to_shuffle)
        
        
        
        
    def print_info(self,show_hand = False, show_playing = False, show_deck= False, show_discard = False): #just for testing
        print()
        print('HAND (', len(self.hand), ')', sep = '')
        if show_hand: print('\t',self.hand)
        
        print('PLAYING (', len(self.playing), ')', sep = '')
        if show_playing: print('\t',self.playing)
        
        print('DECK (', len(self.deck), ')', sep = '')
        if show_deck: print('\t',self.deck)
        
        print('DISCARD (', len(self.discard), ')', sep = '')
        if show_discard: print('\t',self.discard)
        
        print('\n')
        
        
        
def main_test():
    
    testcards = ['copper','copper','copper','copper','copper','copper','copper','estate','estate','estate']
    testgame = DeckSystem(testcards)
    
    
    testgame.print_info(True, True, True, True)
    testgame.draw(5)
    testgame.print_info(True, True, True, True)
    
    testgame.play_card(1)
    testgame.play_card(3)
    testgame.print_info(True, True, True, True)
    testgame.gain_card('cellar')
    testgame.print_info(True, True, True, True)
    
    testgame.discard_cards('playing', 'all')
    testgame.print_info(True, True, True, True)
    testgame.discard_cards('hand', 0)
    testgame.print_info(True, True, True, True)
    
    testgame.discard_cards()
    testgame.print_info(True, True, True, True)
    testgame.shuffle_deck('discard')
    testgame.print_info(True, True, True, True)
    
#main_test()
