# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 13:10:34 2018

@author: mpnun
"""

from board import Board
from player import Player
import numpy as np

class Game:
    
    name_list = ['Bob','Harry','Tom','Jared','Fernando']
    
    def __init__(self, n_players = 2):
        
        self.players = []
        name_inds = np.random.choice(len(Game.name_list),n_players)
        for i in range(n_players):
            self.players.append(Player(name = Game.name_list[name_inds[i]], team=i+1))
        self.board = Board()
    
    def reset(self):
        self.board = Board()
    
    def play_game(self):
        
        game_over = False
        states = []
        
    
        while not game_over:
            
            for p_ind, player in enumerate(self.players):
                if self.board.open_spots == []:
                    print('The game is a draw.')
                    result = 0.5
                    game_over = True
                    break
                else:
                    player.take_turn(self.board)
                    states.append(np.copy(self.board.states))
                    
                    # Check win condition
                    winning_move = self.does_he_win(player)
                    if winning_move:
                        print(player.name + ' wins!')
                        result = p_ind
                        game_over = True
                        break
                    
                self.board.show()
            
        self.board.show()
        
        return np.array(states), result
        
    def does_he_win(self,player):
        owned_spots = (self.board.states.reshape([self.board.n_rows,self.board.n_cols]) == player.team).astype(int)
        col_sums = np.sum(owned_spots,axis=0)
        row_sums = np.sum(owned_spots,axis=1)
        diag_1 = np.sum(np.diag(owned_spots))
        diag_2 = np.sum(np.diag(np.rot90(owned_spots)))
        if 3 in col_sums or 3 in row_sums or diag_1 == 3 or diag_2 == 3:
            return True
        else:
            return False