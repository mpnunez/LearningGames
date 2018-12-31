# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 15:49:18 2018

@author: mpnun
"""

import numpy as np

class Game:
    
    def __init__(self):
        self.pos = 0
        self.pos_history = [self.pos]
        self.keep_playing= True
        
    def reset(self):
        self.pos = 0
        self.pos_history = [self.pos]
        self.keep_playing= True
    
    def play(self):
        while self.keep_playing:
            self.random_move()
        
    def random_move(self):
        if self.pos == 0:
            self.pos = 1
        else:
            r = np.random.randint(0,2)
            if r == 0:
                self.pos += 1
            else:
                self.pos -= 1
        self.pos_history.append(self.pos)
        if self.pos == 4:
            self.keep_playing = False
        

def main():
    
    n = 5
    alpha = 0.5     # learning rate
    gamma = 0.7     # discount rate
    
    
    Q = np.zeros(n)
    Q[n-1] = 1          # last state is winning
    
    adj_states = [[1],[0,2],[1,3],[2,4],[4]]
    def get_future_max(i):
        return np.max(Q[adj_states[i]])
    
    n_trials = 30
    g = Game()
    
    for train_num in range(n_trials):
        
        # Play a game to collect data
        g.play()
        hist = g.pos_history
        g.reset()
        
        # Update the Q table
        hist.reverse()          # put last moves first
        
        # Winning or losing condition
        hist.pop(0)
        
        # Update all other Q values according to the formula
        for inx,state in enumerate(hist):
            Q[state] = (1-alpha) * Q[state] + alpha * gamma * get_future_max(state)
            
        
    print(Q)
        

if __name__ == '__main__':
    main()