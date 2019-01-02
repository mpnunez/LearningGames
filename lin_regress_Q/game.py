# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 10:45:45 2019

@author: mpnun
"""

import numpy as np
import random

class Game(object):
    
    def __init__(self):
        self.state = None                # 
        self.state_history = []       # List of 
        self.keep_playing= True
    
    def record_state(self):
        '''
        Add the current game state to the history list
        '''
        self.state_history.append(np.copy(self.state))
    
    
    def play(self):
        '''
        Make moves until the winning condition is met
        '''
        self.record_state()
        while self.keep_playing:
            self.random_move()
            self.record_state()
            self.keep_playing = not self.check_win_condition()
        
    def random_move(self):
        '''
        Choose a move randomly among the available moves
        '''
        move_list = self.possible_next_states()
        chosen_move = random.choice(move_list)
        self.state = chosen_move     # make the move     
        
    # Could also have methods for choosing moves according to highest Q value - deterministic and probabilistic
    
    
class Maze1D(Game):
    
    def __init__(self):
        Game.__init__(self)
        self.state = 0                
        self.winning_spot = 6
        
        
    def check_win_condition(self,state = None):
        '''
        Game ends when player is on the winning spot
        '''
        if state is None:
            state = self.state
        return self.state == self.winning_spot
        
    
    def possible_next_states(self,state = None):
        '''
        Can move to the left or right
        '''
        if state is None:
            state = self.state
            
        if state <= -2:
            return [state+1]
        elif state >= 10:
            return [state-1]
        else:
            return [state-1, state+1]