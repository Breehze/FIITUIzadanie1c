import genetic,anneal,random, plotting
from typing import List,Tuple,Callable
import argparse

"""Grid Settings"""
CITY_AMOUNT : int = 20
GRID_SIZE : int = 200

"""Simulated Annealing"""

"""Genetic Algorithm"""
MAX_GENERATIONS = 200
MUTATION_CHANCE = 0.05
POPULATION_SIZE = 1000

TOURNAMENT_SIZE = 30
TOURNAMENT_AMOUNT = 10

WINNERS_AMOUNT = 50

parser = argparse.ArgumentParser()
parser.add_argument("-gat","--genetic-algo-tournament",action='store_true')
parser.add_argument("-gar","--genetic-algo-rank",action='store_true')
parser.add_argument("-sa","--simulated-annealing",action='store_true')

args = parser.parse_args()

uniq : Callable = lambda x : x.pop(x.index(random.choice(x)))
tournament : Callable = lambda  current_gen, gen_fitness : genetic.tournament(current_gen,gen_fitness,TOURNAMENT_SIZE,TOURNAMENT_AMOUNT)
rank : Callable = lambda  current_gen, gen_fitness : genetic.rank(current_gen,gen_fitness,WINNERS_AMOUNT)

x : List[int] = [i for i in range(GRID_SIZE)]
y : List[int] = [i for i in range(GRID_SIZE)]

city_locs : List[Tuple[int,int]] = [(uniq(x),uniq(y)) for _ in range(CITY_AMOUNT)]

perm_list  = [index for index in range(CITY_AMOUNT)]
first_gen = [perm_list.copy() for i in range(POPULATION_SIZE)]

[random.shuffle(i) for i  in first_gen]

if args.genetic_algo_tournament:
    path,distance,evolution = genetic.commit_eugenics(first_gen,city_locs,MAX_GENERATIONS,POPULATION_SIZE,MUTATION_CHANCE,tournament)
    plotting.plot_evolution("Some title",evolution)
    plotting.plot_path("Some title",city_locs,first_gen[0],distance)
    plotting.plot_path("Some title",city_locs,path,distance)

if args.genetic_algo_rank:
    path,distance,evolution = genetic.commit_eugenics(first_gen,city_locs,MAX_GENERATIONS,POPULATION_SIZE,MUTATION_CHANCE,tournament)
    plotting.plot_evolution("Some title",evolution)
    plotting.plot_path("Some title",city_locs,first_gen[0],distance)
    plotting.plot_path("Some title",city_locs,path,distance)

if args.simulated_annealing:
    path,distance,evolution = anneal.anneal(first_gen[0],city_locs)
    plotting.plot_evolution("Some title",evolution)
    plotting.plot_path("Some title",city_locs,first_gen[0],distance)
    plotting.plot_path("Some title",city_locs,path,distance)
