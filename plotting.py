import matplotlib.pyplot as plt
from typing import List,Tuple

def plot_path(title : str,city_locs : List[Tuple[int,int]],path,distance: float) -> None:
    route_x = [city_locs[i][0] for i in path] + [city_locs[path[0]][0]]
    route_y = [city_locs[i][1] for i in path] + [city_locs[path[0]][1]]

    plt.figure(figsize=(7, 7))
    plt.plot(route_x, route_y, "-o", c="blue", label="Best route")
    plt.title(f"{title} (Distance = {distance:.2f})")
    plt.legend()
    plt.show()

def plot_evolutions(title : str ,evo_lists : List[Tuple[str,List[float]]]) -> None:
    plt.figure(figsize=(10, 6))
    for evo_list in enumerate(evo_lists):
        plt.plot(evo_list[1][1], label=evo_list[1][0], color=["red","green","blue","cyan","magenta"][evo_list[0]])
    plt.xlabel("Iteration")
    plt.ylabel("Fitness")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
