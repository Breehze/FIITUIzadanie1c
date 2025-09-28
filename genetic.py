import random,math,bisect
from typing import Callable, List,Tuple,Optional
from itertools import accumulate

distance : Callable  = lambda x,y : math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
fitness : Callable = lambda x :1/x

def comp_fitness_array(parent_array : List[List[int]],location_array : List[Tuple[int,int]]) -> List[float]:
    assert len(parent_array)   
    fitness_array : List[float] = []
    
    for parent in  parent_array:
        parent_len : int = len(parent)
        
        path_distance : float = sum([distance(location_array[parent[i]],location_array[parent[i+1]]) for i in range(parent_len-1)])
        path_distance += distance(location_array[parent[0]],location_array[parent[-1]])
        
        fitness_array.append(fitness(path_distance))
        
    return fitness_array

def tournament(population : List[List[int]], scored_population : List[float] , participants : int,tournament_amount : int) -> List[List[int]]:
    assert len(population) == len(scored_population)
    
    winners : List[List[int]] = []
    for _ in range(tournament_amount):
        part_ind : List[int]  = [random.randint(0,len(population)-1) for _ in range(participants)]
        winner : int =  max(part_ind, key=lambda i: scored_population[i])
        winners.append(population[winner])
    return winners

def rank(population : List[List[int]], scored_population : List[float] , winners_amount : int) -> List[List[int]]:
    sorted_population = sorted(zip(population, scored_population), key=lambda x: x[1])   
    ranks = list(range(1, len(sorted_population)+1)) 
    total_rank = sum(ranks)
    
    accd = list(accumulate(ranks))
    
    winners = []
    for _ in range(winners_amount):
        idx = bisect.bisect_left(accd, random.uniform(0,total_rank))
        winners.append(sorted_population[idx][0])   
    return winners

def crossover(parent_a : List[int] ,parent_b : List[int]):
    assert len(parent_a) == len(parent_b)
    assert len(parent_a) > 4
    
    genome_split1 : int = random.randrange(1,len(parent_a)//2)
    genome_split2 : int = random.randrange(len(parent_a)//2,len(parent_a)-1)
    
    parts_a : List[int] =  parent_a[genome_split1:genome_split2]
    parts_b : List[int]  = parent_b[genome_split1:genome_split2]
    
    child_a : List[int]  = [gene for gene in parent_a if gene not in parts_b]
    child_a[genome_split1:genome_split1] = parts_b

    child_b : List[int] = [gene for gene in parent_b if gene not in parts_a]
    child_b[genome_split1:genome_split1] = parts_a
    
    return child_a,child_b

def mutate(genome: List[int]) -> List[int]:
    assert len(genome) > 2 
    swap1, swap2 = random.sample(range(len(genome)), 2)
    genome[swap1:swap2] = reversed(genome[swap1:swap2])  
    #genome[swap1], genome[swap2] = genome[swap2], genome[swap1]
    return genome

def commit_eugenics(
    initial_gen :List[List[int]], 
    city_locations :List[Tuple[int,int]], 
    max_generations :int, 
    population_size_per_gen :int, 
    mutation_chance :float , 
    selection_func :Callable
) -> Tuple[List[int],float,List[float]]:
    
    current_gen = initial_gen
    fitness_evo : List[float] = []
    for _ in range(max_generations):
        gen_fitness = comp_fitness_array(current_gen, city_locations)
        fitness_evo.append(max(gen_fitness))
        winners = selection_func(current_gen, gen_fitness)

        next_gen = []
        while len(next_gen) < population_size_per_gen:
            parent_a, parent_b = random.sample(winners, 2)
            child_a, child_b = crossover(parent_a, parent_b)

            if random.random() < mutation_chance:
                child_a = mutate(child_a)
            if random.random() < mutation_chance:
                child_b = mutate(child_b)

            next_gen.extend([child_a, child_b])

        current_gen = next_gen[:population_size_per_gen]

    final_fitness = comp_fitness_array(current_gen, city_locations)
    best_index = final_fitness.index(max(final_fitness))
    
    return  current_gen[best_index] , fitness(final_fitness[best_index]), fitness_evo #xd
