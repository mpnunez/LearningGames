# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 17:46:15 2018

@author: mpnun
"""

import numpy as np
from sklearn.neural_network import MLPRegressor
from tensorflow import keras
import tensorflow as tf
import matplotlib.pyplot as plt
import sys

def main():
    
    print('Train the model')
    X = np.load('X.npy')
    Y = np.load('Y.npy')
    
    # Feature engineering
    player_one_spot = (X == 1).astype(int)
    player_two_spot = (X == 2).astype(int)
    empty_spot = (X == 0).astype(int)
    X = np.hstack([player_one_spot, player_two_spot, empty_spot])
    Y = Y * 2 - 1
    
    model = keras.Sequential([keras.layers.Dense(18, activation=tf.nn.relu),keras.layers.Dense(1)])
    
    optimizer = tf.train.RMSPropOptimizer(0.001)

    model.compile(loss='mse',optimizer=optimizer, metrics=['mae', 'mse'])
    
    model.fit(X, Y, epochs=3)
    example_result = model.predict(X)

    plt.figure()
    plt.xlabel('Train')
    plt.ylabel('Neural Network')
    plt.plot(Y, example_result,'o')
  

if __name__ == '__main__':
    main()