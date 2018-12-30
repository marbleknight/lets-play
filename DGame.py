# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 15:45:05 2018

@author: edavis
"""
debug = True
import DeckSystem

class DGame():
    
    
    def __init__(self):
        self.starting_deck = ['copper','copper','copper','copper','copper','copper','copper','estate','estate','estate']
        self.build_playing_field()
        
        self.players = []
        
        self.player1 = DeckSystem.DeckSystem(self.starting_deck)
        
        
    def build_playing_field(self):
        #a library of all the cards
        self.dominion_deck = {'money':{'copper': {'cost': 0, 'available': 100}, 
                                   'silver': {'cost': 3, 'available': 100}, 
                                   'gold': {'cost': 6, 'available': 100} }, 
                          'land': {'estate': {'cost': 2, 'available': 100},
                                   'duchy': {'cost': 5, 'available': 10},
                                   'province': {'cost': 8, 'available': 10} } }
        #deck of cards used in this game
        self.game_deck = {}
    
        for card in self.dominion_deck['money']:
            self.game_deck[card] = self.dominion_deck['money'][card] #add it to the game deck
        for card in self.dominion_deck['land']:
            self.game_deck[card] = self.dominion_deck['land'][card] #add it to the game deck
        
    
    
    def buy_phase(self, player, buys = 1):
        #count money 
        money = self.count_money(player)
        if debug: print('start money:', money)
        keep_buying = True
        fails = 0 #if they fail too many times, their turn just ends
    
        while buys > 0 and keep_buying == True:
            #get selection
            selection = 'silver'
            #selection = input('What card do you want?') #needs fixing. Big crashable feature!!!!! for next teir????
            
            purchase = self.buy_card(player, money, selection)
            money = purchase[0]
            success = purchase[1]
            if success: buys -=1 #if they buy something, used up a purchase
            else:
                fails +=1
                if fails > 2: keep_buying = False #three strikes, your out!
            #get keep_buying?
        #stops if: runs out of buys or player decides to stop or if they fail too many times
    
    
    def buy_card(self, player, money, selection):
        cost = self.game_deck[selection]['cost'] #get the cost from the dictionary
        available = self.game_deck[selection]['available']
        
        if money >= cost and available > 0: #purchase okay
            player.gain_card(selection)
            money -= cost
            if debug: print('money left:', money)
            purchased = True
            self.game_deck[selection]['available'] -= 1 #a card leaves the pile
        else:
            if debug: print('costs too much, nothing purchased')
            purchased = False
            
        return [money, purchased]
    
    
    def count_money(self, player):
        money = 0
        for i in range(len(player.hand)): #go through their whole hand and count out the money
            if player.hand[i] == 'copper':
                money +=1
            elif player.hand[i] == 'silver':
                money +=2
            elif player.hand[i] == 'gold':
                money +=3        
            #add any other types of money here    
        return money
    
    
    def end_turn(self, player): 
        #discard everything and draw
        player.discard_cards('hand', 'all')
        player.discard_cards('playing','all')
        
        for i in range(5):
            try: player.draw()
            except: 
                player.shuffle_deck('discard')
                player.draw()
        player.turns_played +=1
        
    
    def do_turn(self, player):
        if debug: print('TURN #', player.turns_played+1, sep='')
        #play action cards
            #shuffle if needed
        self.buy_phase(player)
        self.end_turn(player)
        
            
        
        
        


def main_test():
    
    starting_deck = ['copper','copper','copper','copper','copper','copper','copper','estate','estate','estate']
    
    player1 = DeckSystem.DeckSystem(starting_deck)
    player2 = DeckSystem.DeckSystem(starting_deck)
    
    player1.print_info(show_deck = True)
    player2.print_info(show_deck = True)
    
    game = DGame()
    print(game.game_deck)
    
def main_test2():
    game = DGame()
    game.player1.print_info(True,True,True,True)
    
    purchase = True
    response = game.buy_card(game.player1, 10, 'fake card', 3)
    money = response[0]
    while purchase == True:
        response = game.buy_card(game.player1, money, 'fake card', 3)
        money = response[0]
        purchase = response[1]
    
    game.player1.print_info(True,True,True,True)
    
    
def main_test3():
    game = DGame()
    game.player1.draw(5)
    game.player1.print_info(True,True,True,True)
    
    game.buy_phase(game.player1, buys = 20) #second to last
    
    game.player1.print_info(True,True,True,True)
    
    game.end_turn(game.player1) #last function
    
    game.player1.print_info(True,True,True,True)
    
    print (game.game_deck)
    
    
def main_test4():
    game = DGame()
    game.player1.draw(5)
    game.player1.print_info(True,True,True,True)
    
    for i in range(5):
        game.do_turn(game.player1)
        game.player1.print_info(True,True,True,True)
        #input('<press enter to continue>')
    
    game.player1.shuffle_deck('all')
    print('Player bought', game.player1.deck.count('silver'), 'silvers')
    
main_test4()
    
"""
Still need:
    Everything to do with Action Phase
    A way to retrieve the selection during buy_phase
    A way to switch from player to player 
    ...and more, I'm sure
    
"""    
