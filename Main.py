"""

@author: Hamed Taghadosi
"""


import numpy as np
import random as rnd
import copy
from Gen import N_queen



        
#randomly initialize firt population
def Fist_random_inittlize_population(population_size, n_queen = 8):
    Gens = []
    Gens_value = []
    for i in range(population_size):
        chromosome = N_queen(n_queen)
        Gens.append(copy.copy(chromosome)) #add  a new chromosome to our population
        Gens_value .append(copy.copy(chromosome.eval))# add coresponding rate of that chromosome
    
    return Gens, Gens_value
        
#setting new parameter to new population    
def Change_generation( gens , gens_rate):
    Gens = gens
    Gens_value = gens_rate
    return Gens , Gens_value
    
#selecting parent
def Parent_selection(population_size,population_pool):
    selected_parent = []
    selected_parent_rate = []
    for i in range( int(population_size / 2) ):
        selected = []
        selected_rate = []
        for j in range(5):# select 5th chromosome randomly
            random = rnd.randint(0,population_size-1)
            selected.append(population_pool[random])
            selected_rate.append(population_pool[random].eval)
            
        #select 2 index of best from 5 th
        max1 = max(selected_rate)
        max1 = selected_rate.index(max1)
        selected_rate[max1] = -5000
        max2 = max(selected_rate)
        max2 = selected_rate.index(max2)
        #adding them to the next future
        
        selected_parent.append(selected[max1])
        selected_parent_rate.append(selected[max1].eval)
        selected_parent.append(selected[max2])
        selected_parent_rate.append(selected[max2].eval)
        
    return selected_parent , selected_parent_rate
        

            
            
#cross and cut cross over
def Child_creation(population_size, selected_parent , population_pool_rate , population_pool):
    for j in range(int((population_size-1) / 2) , 2 ):
        #print(j)
        parent1_board = copy.copy(selected_parent[j].bred)
        parent2_board = copy.copy(selected_parent[j+1].bred)
        parent1_board_copy = copy.copy(parent1_board) 
        Temp1 = parent2_board[np.random.randint(0,7,[4])] # chosing 4th random of parent 2 and replace it in parent1
        Temp2 = parent1_board_copy[np.random.randint(0,7,[4])]#chosing 4th random of parent 1 and replace it in parent2
        parent1_board[4:] = Temp1
        parent2_board[4:] = Temp2


        selected_parent[j].create(parent1_board)
        selected_parent[j+1].create(parent2_board)
        
        
        # evaluating new childs
        selected_parent[j].evaluate()
        selected_parent[j+1].evaluate()
        
        
        # finding 2 one of the worst perivious generation
        min1 = min(population_pool_rate)
        min1 = population_pool_rate.index(min1)
        population_pool_rate[min1] = -85656
        min2 = min(population_pool_rate)
        min2 = population_pool_rate.index(min2) 
        
        #replace new child to those worst
        population_pool[min1] = copy.copy(selected_parent[j])
        population_pool_rate[min1] = selected_parent[j].eval
        population_pool[min2] = copy.copy(selected_parent[j+1])
        population_pool_rate[min2] = selected_parent[j+1].eval
        
        
        

    population_pool_rate , population_pool = sort(population_pool_rate , population_pool , population_size)
    return population_size, selected_parent , population_pool_rate , population_pool



#Swaping 2 position
def mutation(child):
    chiild_board = child.chest
    index = np.random.randint(0,7,[2]) # chose 2 condidate chest for swap
    temp = copy.copy(chiild_board[index[0]])
    # swap 2 queen
    chiild_board[index[0]] = chiild_board[index[1]]
    chiild_board[index[1]] = temp
    #evalue new child
    child.create(chiild_board)
    child.evaluate()
    
    return child , child.eval

def sort(current_gen_rate , Gens , population_size):
    next_gen_sort = []
    next_gen_sort_rate =[]
    for i in range(population_size):
        temp = max(current_gen_rate)
        temp = current_gen_rate.index(temp)
        
        next_gen_sort.append(Gens[temp])
        next_gen_sort_rate.append(Gens[temp].eval)
        current_gen_rate[temp] = -10000
    
    Gens , Gens_rate = Change_generation(next_gen_sort , next_gen_sort_rate)
    
    return Gens_rate , Gens 
    






    

                
    
