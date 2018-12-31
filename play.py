# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 10:55:33 2018
4
@author: mpnun
"""

from game import Game
import numpy as np

def main():
    
    
    
    
    z = Game()
    
    X = []
    Y = []
    
    n_games = 10000
    for i in range(n_games):
        print(i)
        z.reset()
        states, result = z.play_game()
        X.append(states)
        new_Y = assign_Q_values(states,result)
        Y = Y + new_Y
        
        
    X = np.vstack(X)
    Y = np.array(Y)
    np.save('X.npy',X)
    np.save('Y.npy',Y)
    print(X)
    print(Y)


def assign_Q_values(states,result):
    p = 0.3
    n_moves = states.shape[0]
    Y = []
    if result == 0.5:
        for j in range(n_moves):
            Y.append(result)
    else:
        Y = [result,result]     # The value of the last two moves are certain
        
        for i in range(n_moves-2):
            Y.append( p * Y[-1] + (1-p) * 0.5)
            Y.reverse()
        
    return Y

if __name__ == '__main__':
    main()