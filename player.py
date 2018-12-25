# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 13:10:35 2018

@author: mpnun
"""

import random

class Player:
    
    def __init__(self,name = 'Bob',team=1):
        self.name = name
        self.team = team
    
    def take_turn(self,board):
        print(self.name + ' is taking his trun')
        spot_to_take = random.choice(board.open_spots)
        board.states[spot_to_take] = self.team
        board.open_spots.remove(spot_to_take)