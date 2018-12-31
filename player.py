# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 13:10:35 2018

@author: mpnun
"""

import random
import numpy as np

class Player:
    
    def __init__(self,name = 'Bob',team=1):
        self.name = name
        self.team = team
    
    def take_turn(self,board):
        #print(self.name + ' is taking his trun')
        spot_to_take = self.choose_spot(board)
        board.states[spot_to_take] = self.team
        board.open_spots.remove(spot_to_take)
        
    def choose_spot(self,board):
        spot_to_take = random.choice(board.open_spots)
        return spot_to_take
        
    
class HumanPlayer(Player):
    
    def __init__(self,name = 'Bob',team=1):
        Player.__init__(self, name = name, team=team)
        
    def choose_spot(self,board):
        no_legal_move = True
        while no_legal_move:
            spot_to_take = int(input('Spot to take: '))
            if spot_to_take in board.open_spots:
                no_legal_move = False
        return spot_to_take
    
    
class AIPlayer(Player):
    
    def __init__(self,name = 'Bob',team=1):
        Player.__init__(self, name = name, team=team)
        
    def choose_spot(self,board):
        
        Q_vals = np.zeros(len(board.open_spots))
        for ind, possible_move in enumerate(board.open_spots):
            new_board = np.copy(board.states)
            new_board[possible_move] = self.team            # make the theoretical move
            Q_vals[ind] = self.compute_Q(new_board)                 # value of new board
            
        spot_to_take = board.open_spots[np.argmax(Q_vals)]
        return spot_to_take
    
    def compute_Q(self,new_board):
        return 0.5
    
    