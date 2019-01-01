# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 10:45:45 2019

@author: mpnun
"""

import numpy as np
import random

class Game:
    
    def __init__(self):
        self.pos = np.zeros([3,3])
        self.pos_history = []
        self.keep_playing= True
    
    def record_state(self):
        self.pos_history.append(np.copy(self.pos))
    
    
    def play(self):
        self.record_state()
        print(self.pos)
        while self.keep_playing:
            self.random_move()
            self.record_state()
            self.keep_playing = not self.check_win_condition()
            print(self.pos)
        
    def random_move(self):
        
        move_list = self.possible_next_states()
        chosen_move = random.choice(move_list)
        self.pos[chosen_move[0],chosen_move[1]] = 1     # make the move     
        
            
    def check_win_condition(self):
        return 3 in np.sum(self.pos,axis = 0) or 3 in np.sum(self.pos,axis = 1)
        
    
    def possible_next_states(self):
        return [i for i in np.transpose(np.array(np.where(self.pos==0)))]