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
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
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
            

def update_matrix(mat,indices):
    x = np.copy(mat)
    x[indices[0],indices[1]] = 1
    return x

class Q_evaluator:
    
    def __init__(self):
        
        self.alpha = 0.5     # learning rate
        self.gamma = 0.7     # discount rate
        self.state_list = []
        self.Y = []                 # Q values to regress
        self.NN = None
        
        
    def initialize_NN(self): 
        self.NN = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                            tf.keras.layers.Dense(200, activation=tf.nn.relu),
                                            tf.keras.layers.Dense(1)])
        self.NN.compile(optimizer='adam',loss='mse',metrics=['accuracy'])     
    
    def train_NN(self):
        X = np.array(self.state_list)
        self.NN.fit(X, self.Y, epochs=5)
    
    def predict_Q(self,state):      # We will need this to call the neural network model
        return np.sum(state) / 9.
    
    def get_future_max(self,state):
        
        open_moves = [i for i in np.transpose(np.array(np.where(state==0)))]
        next_states = [update_matrix(state,move) for move in open_moves]
        return np.max([self.predict_Q(i) for i in next_states])
    
 
    def update_Q(self,state):
        return (1-self.alpha) * self.predict_Q(state) + self.alpha * self.gamma * self.get_future_max(state)
    

def main():
    
    n_trials = 1
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
        
        Qobj.Y = Qobj.Y + y_vec             # Add q values
    
    print(Qobj.state_list)
    print(Qobj.Y)

if __name__ == '__main__':
    main()