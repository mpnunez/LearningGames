# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 10:45:47 2019

@author: mpnun
"""


import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import random

def update_matrix(mat,indices):
    x = np.copy(mat)
    x[indices[0],indices[1]] = 1
    return x

class Q_evaluator:
    
    def __init__(self):
        
        self.alpha = 0.5     # learning rate
        self.gamma = 0.7     # discount rate
        self.state_list = []
        self.Y_list = []                 # Q values to regress
        self.NN = None
        
        
    def initialize_NN(self): 
        self.NN = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                            tf.keras.layers.Dense(200, activation=tf.nn.relu),
                                            tf.keras.layers.Dense(1)])
        self.NN.compile(optimizer='adam',loss='mse',metrics=['accuracy'])     
    
    def train_NN(self):
        X = np.array(self.state_list)
        Y = np.array(self.Y_list)
        self.NN.fit(X, self.Y, epochs=5)
    
    def predict_Q(self,state):      # We will need this to call the neural network model
        return np.sum(state) / 9.
    
    def get_future_max(self,state):
        
        open_moves = [i for i in np.transpose(np.array(np.where(state==0)))]
        next_states = [update_matrix(state,move) for move in open_moves]
        return np.max([self.predict_Q(i) for i in next_states])
    
 
    def update_Q(self,state):
        return (1-self.alpha) * self.predict_Q(state) + self.alpha * self.gamma * self.get_future_max(state)
    