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

from game import Maze1D
from q_evaluator import Q_evaluator_1Dmaze


def main():
    
    n_trials = 1000                  # number of games to play
    retrain_every = 10              # retrain neural network after 
    Qobj = Q_evaluator_1Dmaze()
    
    for train_num in range(n_trials):

        # Play a game to collect data
        g = Maze1D()
        g.play()
        hist = g.state_history
        
        # Get data for the final state and second to last state
        hist.reverse()          # put last moves first
        Qobj.state_list = Qobj.state_list + hist
        y_vec = [1]
        hist.pop(0)
        y_vec.append(Qobj.update_Q(g,hist[0],future_max=y_vec[0]))
        hist.pop(0)
        
        # Update the Q table for the rest of the moves
        for idx, state in enumerate(hist):
            y_vec.append(Qobj.update_Q(g,state))
        
        Qobj.Y_list = Qobj.Y_list + y_vec             # Add q values
    
        if ((train_num+1) % retrain_every) == 0:
            Qobj.train_NN()         # Use the newest data to train the neural network
            Qobj.clear_data()
    
    x_vec = np.array([-2,-1,0,1,2,3,4,5,6])
    y_vec = np.array([Qobj.predict_Q(i) for i in x_vec])
    
    print(y_vec)

if __name__ == '__main__':
    main()