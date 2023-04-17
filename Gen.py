"""

@author: ThuAlfeqr_AlBkhati
"""

import numpy as np
import random as rnd
import copy

class N_queen():
    #constructor of model
    def __init__(self , n_queen = 8):
        #create chest of game
        super(N_queen, self).__init__()
        self.chest = np.arange(n_queen)
        rnd.shuffle(self.chest)
        self.evaluate()
    
    #setting a new to a chromosome
    def create(self,board):
        self.chest = board
    #Fitness function of chromosome
    def evaluate(self):
        
        #this function was getten from github 
        checks = 0
        
        row_col_clashes = abs(len(self.chest) - len(np.unique(self.chest)))
        checks += row_col_clashes
        
        # calculate diagonal clashes
        for i in range(len(self.chest)):
            for j in range(len(self.chest)):
                if ( i != j):
                    dx = abs(i-j)
                    dy = abs(self.chest[i] - self.chest[j])
                    if(dx == dy):
                        checks += 1
        
        
        self.eval = -1 * (checks / 2)