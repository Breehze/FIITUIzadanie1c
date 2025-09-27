import random,math
from typing import Callable,List,Tuple

distance : Callable  = lambda x,y : math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def two_opt_move(path: List[int]):
    new_path = path.copy()
    point_a, point_b = sorted(random.sample(range(len(path)), 2))
    new_path[point_a:point_b+1] = new_path[point_a:point_b+1][::-1]   
    return new_path

def compute_path_length(path : List[int],city_locations : List[Tuple[int,int]]):
    path_distance : float = sum([distance(city_locations[path[i]],city_locations[path[i+1]]) for i in range(len(path)-1)])
    path_distance += distance(city_locations[path[0]],city_locations[path[-1]])
    return path_distance

def anneal(initial_permutation : List[int],city_locations : List[Tuple[int,int]])  -> Tuple[List[int],float]:
    current = initial_permutation 
    best = current
    current_distance = compute_path_length(current,city_locations)
    best_distance = current_distance

    T = 100
    alpha = 0.99
    min_T = 1e-6

    while T > min_T:
        candidate = two_opt_move(current)#swap_pos(current)
        candidate_distance = compute_path_length(candidate,city_locations)
        delta = candidate_distance - current_distance

        if delta < 0 or random.random() < math.exp(-delta / T):
            current = candidate
            current_distance = candidate_distance

        if current_distance < best_distance:
            best = current
            best_distance = current_distance

        T *= alpha

    return best,best_distance
