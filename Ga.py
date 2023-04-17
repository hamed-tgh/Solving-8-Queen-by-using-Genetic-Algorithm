"""

@author: ThuAlfeqr_AlBkhati
"""

from operation import sort,mutation,Child_creation,Parent_selection,Change_generation,Fist_random_inittlize_population
import random as Random
import copy 
import numpy as np

#Genetic algorithm

population_pool =[]
population_pool_rate = []
selected_parent = []
selected_parent_rate = []
population_pool, population_pool_rate = Fist_random_inittlize_population(100)
solution= []
for epoche in range(10000):
    #print(iteration)
    # selecting suitable parents
    selected_parent , selected_parent_rate =  Parent_selection(100,population_pool)
    population_pool_rate , population_pool  = sort(population_pool_rate , population_pool , 100)

       
    population_size, selected_parent , population_pool_rate , population_pool = Child_creation(100, selected_parent , population_pool_rate , population_pool)
    #mutation
    for j in range(population_size):
        chance_mute = Random.random() # chance for mutation
        if chance_mute <= 0.8 :
             population_pool[j]  , population_pool_rate[j]= copy.copy(mutation(population_pool[j]))
    
    # chech if a  solution appear in curent population we return it 
    if 0 in population_pool_rate:
        temp = population_pool_rate.index(0)
        solution.append(copy.copy(population_pool[temp]))
        print("added")
        break


print("Finish")
print("GA Find {0} as final result ".format(solution[0].chest)  )
#print("number of checks in this solution is: {0} ".format(solution[0].eval) )

chest = np.zeros([8,8])
for j in range(8):
    chest[j , solution[0].chest[j] ]  = 1

print(chest)

        
#            create(copy.copy(next_gen))
        
