# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 13:10:33 2018

@author: mpnun
"""

import numpy as np

class Board:
    
    def __init__(self, n_rows = 3, n_cols = 3):
        
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.open_spots = [i for i in range(n_rows*n_cols)]
        self.states = np.zeros([n_rows*n_cols])
        
        
    def show(self):
        print(self.states.reshape([self.n_rows,self.n_cols]))