# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 16:57:42 2018

@author: mpnun
"""

'''
One player tic tac toe
Q learning uses a neural network
'''

import numpy as np

from Game2 import Game
from q_evaluator import Q_evaluator


def main():
    
    n_trials = 100                  # number of games to play
    retrain_every = 10              # retrain neural network after 
    Qobj = Q_evaluator()
    
    for train_num in range(n_trials):
        
        # Play a game to collect data
        g = Game()
        g.play()
        hist = g.pos_history
        
        # Get data for the final state
        hist.reverse()          # put last moves first
        Qobj.state_list = Qobj.state_list + hist
        y_vec = [1]
        hist.pop(0)
        
        # Update the Q table for the rest of the moves
        for idx, state in enumerate(hist):
            y_vec.append(Qobj.update_Q(state))
        
        Qobj.Y_list = Qobj.Y_list + y_vec             # Add q values
    
        if ((train_num+1) % retrain_every) == 0:
            Qobj.
    
    print(Qobj.state_list)
    print(Qobj.Y_list)

if __name__ == '__main__':
    main()