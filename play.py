# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 10:55:33 2018

@author: mpnun
"""

from game import Game
import numpy as np

def main():
    
    z = Game()
    
    X = []
    Y = []
    
    n_games = 10
    for i in range(n_games):
        z.reset()
        states, result = z.play_game()
        X.append(states)
        for j in range(states.shape[0]):
            Y.append(result)
        
    print(X)
    X = np.vstack(X)
    Y = np.array(Y)
    np.save('X.npy',X)
    np.save('Y.npy',Y)
    print(X)
    print(Y)

if __name__ == '__main__':
    main()