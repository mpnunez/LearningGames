# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 10:45:47 2019

@author: mpnun
"""


import numpy as np
#import tensorflow as tf
#from tensorflow import keras
#from tensorflow.keras import layers

def update_matrix(mat,indices):
    x = np.copy(mat)
    x[indices[0],indices[1]] = 1
    return x

class Q_evaluator(object):
    
    def __init__(self):
        
        self.alpha = 0.5            # learning rate
        self.gamma = 0.7            # discount rate
        self.state_list = []        # states to regress -> makes X
        self.Y_list = []            # Q values to regress -> makes Y
        self.model_trained = False
        

    def predict_Q(self,state,isfinal=False):      # We will need this to call the neural network model
        if isfinal:
            return 1
        else:
            if self.model_trained:
                return self.call_NN(state)   #call the fitted model
            else:   
                return 0.5                  # Initial Q values
    
    def get_future_max(self,game,state):
        '''
        Find maximum Q value among all possible next states
        '''
        next_states = game.possible_next_states(state = state)
        return np.max([self.predict_Q(i) for i in next_states])
    
 
    def update_Q(self,game,state,future_max=None):
        if future_max is None:
            future_max = self.get_future_max(game,state)
        return (1-self.alpha) * self.predict_Q(state) + self.alpha * self.gamma * future_max

    def clear_data(self):
        '''
        Erase previous data
        '''
        self.state_list = []        # states to regress -> makes X
        self.Y_list = []            # Q values to regress -> makes Y


class Q_evaluator_1Dmaze(Q_evaluator):
    
    def __init__(self):
        Q_evaluator.__init__(self)
        
    def initialize_NN(self): 
        self.a = None
        self.b = None
    
    def train_NN(self):
        X = np.array(self.state_list)
        Y = np.log(np.array(self.Y_list))
        coeffs = np.polyfit(X, Y, 1)
        self.a = coeffs[0]
        self.b = coeffs[1]
        self.model_trained = True
        
    def call_NN(self,x):
        return np.exp(self.a * x + self.b)
        

'''
class Q_evaluator_1Dmaze(Q_evaluator):
    
    def __init__(self):
        Q_evaluator.__init__(self)
        
    def initialize_NN(self): 
        self.model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                            tf.keras.layers.Dense(200, activation=tf.nn.relu),
                                            tf.keras.layers.Dense(1)])
        self.model.compile(optimizer='adam',loss='mse',metrics=['accuracy'])     
    
    def train_NN(self):
        X = np.array(self.state_list)
        Y = np.array(self.Y_list)
        self.model.fit(X, Y, epochs=5)
'''