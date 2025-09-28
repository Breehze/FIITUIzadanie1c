import genetic,anneal,random, plotting
from typing import List,Tuple,Callable
import argparse

""" Musim spravit  plot pre fitness evoluciu
    Argy na switchovanie  
    Casovanie ???
"""

"""Grid Settings"""
CITY_AMOUNT : int = 20
GRID_SIZE : int = 200

"""Simulated Annealing"""

"""Genetic Algorithm"""
MAX_GENERATIONS = 100
MUTATION_CHANCE = 0.05
POPULATION_SIZE = 1000

TOURNAMENT_SIZE = 30
TOURNAMENT_AMOUNT = 10

WINNERS_AMOUNT = 100

uniq : Callable = lambda x : x.pop(x.index(random.choice(x)))
tournament : Callable = lambda  current_gen, gen_fitness : genetic.tournament(current_gen,gen_fitness,TOURNAMENT_SIZE,TOURNAMENT_AMOUNT)
rank : Callable = lambda  current_gen, gen_fitness : genetic.rank(current_gen,gen_fitness,WINNERS_AMOUNT)

x : List[int] = [i for i in range(GRID_SIZE)]
y : List[int] = [i for i in range(GRID_SIZE)]

city_locs : List[Tuple[int,int]] = [(uniq(x),uniq(y)) for _ in range(CITY_AMOUNT)]

perm_list  = [index for index in range(CITY_AMOUNT)]
first_gen = [perm_list.copy() for i in range(POPULATION_SIZE)]

[random.shuffle(i) for i  in first_gen]

#path,distance,hello = genetic.commit_eugenics(first_gen,city_locs,MAX_GENERATIONS,POPULATION_SIZE,MUTATION_CHANCE,tournament)
a,b,c = anneal.anneal(first_gen[0],city_locs)
