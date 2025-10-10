import random,math
from typing import Callable,List,Tuple

distance : Callable  = lambda x,y : math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def swap_pos(path: List[int]) -> List[int]:
    new_path = path.copy()
    point_a, point_b = sorted(random.sample(range(len(path)), 2))
    new_path[point_a:point_b+1] = reversed(new_path[point_a:point_b+1])
    return new_path

def compute_path_length(path : List[int],city_locations : List[Tuple[int,int]]) -> float:
    path_distance : float = sum([distance(city_locations[path[i]],city_locations[path[i+1]]) for i in range(len(path)-1)])
    path_distance += distance(city_locations[path[0]],city_locations[path[-1]])
    return path_distance

def anneal(
    initial_permutation : List[int],
    city_locations : List[Tuple[int,int]],
    initial_temp:float,
    cooling_rate : float,
    min_temp: float, 
) -> Tuple[List[int],float,List[float]]:
    
    distance_evo : List[float] = []
    current = initial_permutation 
    best = current
    current_distance = compute_path_length(current,city_locations)
    best_distance = current_distance
    
    while initial_temp > min_temp:
        candidate = swap_pos(current)
        candidate_distance = compute_path_length(candidate,city_locations)
        delta = candidate_distance - current_distance

        if delta < 0 or random.random() < math.exp(-delta / initial_temp):
            current = candidate
            current_distance = candidate_distance

        if current_distance < best_distance:
            best = current
            best_distance = current_distance
            distance_evo.append(1/best_distance)

        initial_temp *= cooling_rate 

    return best,best_distance,distance_evo
