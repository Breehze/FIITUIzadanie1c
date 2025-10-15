import genetic,anneal,random, plotting
from typing import List,Tuple,Callable
import argparse

"""Grid Settings"""
CITY_AMOUNT : int = 20
GRID_SIZE : int = 200

"""Simulated Annealing"""
INITIAL_TEMP : float = 1000
MINIMAL_TEMP : float = 1e-6
COOLING_RATE : float = 0.9995

"""Genetic Algorithm"""
MAX_GENERATIONS : int = 1000
MUTATION_CHANCE : float = 0.05
POPULATION_SIZE : int = 200

TOURNAMENT_SIZE : int = 35
TOURNAMENT_AMOUNT : int = 5

WINNERS_AMOUNT : int = 25

parser = argparse.ArgumentParser()
parser.add_argument("-gat","--genetic-algo-tournament",action='store_true')
parser.add_argument("-gar","--genetic-algo-rank",action='store_true')
parser.add_argument("-sa","--simulated-annealing",action='store_true')
parser.add_argument("-d","--debug",action='store_true')
parser.add_argument("-m","--mutation")

args = parser.parse_args()

random.seed(1) if args.debug else None

uniq : Callable = lambda x : x.pop(x.index(random.choice(x)))
tournament : Callable = lambda  current_gen, gen_fitness : genetic.tournament(current_gen,gen_fitness,TOURNAMENT_SIZE,TOURNAMENT_AMOUNT)
rank : Callable = lambda  current_gen, gen_fitness : genetic.rank(current_gen,gen_fitness,WINNERS_AMOUNT)

x : List[int] = [i for i in range(GRID_SIZE)]
y : List[int] = [i for i in range(GRID_SIZE)]

city_locs : List[Tuple[int,int]] = [(uniq(x),uniq(y)) for _ in range(CITY_AMOUNT)]

perm_list  = [index for index in range(CITY_AMOUNT)]
first_gen = [perm_list.copy() for i in range(POPULATION_SIZE)]

[random.shuffle(i) for i  in first_gen]

evolutions : List[Tuple] = []

random.seed() if args.debug else None

mutate_table = {
    "swap" : genetic.mutate_swap_pos,
    "reverse" : genetic.mutate_reverse_subseg
}

mutation_func : Callable  = mutate_table[args.mutation] if args.mutation else genetic.mutate_swap_pos

if args.genetic_algo_tournament:
    path,distance,evolution = genetic.commit_eugenics(first_gen,city_locs,MAX_GENERATIONS,POPULATION_SIZE,MUTATION_CHANCE,tournament,mutation_func)
    plotting.print_info(path,distance)
    evolutions.append(("GAT",evolution))
    plotting.plot_path("First Gen",city_locs,first_gen[0],anneal.compute_path_length(first_gen[0],city_locs))
    plotting.plot_path("Genetic algorithm - Tournament",city_locs,path,distance)

if args.genetic_algo_rank:
    path,distance,evolution = genetic.commit_eugenics(first_gen,city_locs,MAX_GENERATIONS,POPULATION_SIZE,MUTATION_CHANCE,rank,mutation_func)
    plotting.print_info(path,distance)
    evolutions.append(("GAR",evolution))
    plotting.plot_path("First Gen",city_locs,first_gen[0],anneal.compute_path_length(first_gen[0],city_locs))
    plotting.plot_path("Genetic algorithm - Rank",city_locs,path,distance)

if args.simulated_annealing:
    path,distance,evolution = anneal.anneal(first_gen[0],city_locs,INITIAL_TEMP,COOLING_RATE,MINIMAL_TEMP)
    plotting.print_info(path,distance)
    evolutions.append(("SA",evolution))
    plotting.plot_path("Starting point",city_locs,first_gen[0],anneal.compute_path_length(first_gen[0],city_locs))
    plotting.plot_path("Simulated Annealing",city_locs,path,distance)

plotting.plot_evolutions("Fitness evolution",evolutions) if args.genetic_algo_tournament or args.genetic_algo_rank or args.simulated_annealing else None
