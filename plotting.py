import matplotlib.pyplot as plt
from typing import List,Tuple

def plot_path(title : str,city_locs : List[Tuple[int,int]],path,distance: float) -> None:
    route_x = [city_locs[i][0] for i in path] + [city_locs[path[0]][0]]
    route_y = [city_locs[i][1] for i in path] + [city_locs[path[0]][1]]

    plt.figure(figsize=(7, 7))
    plt.scatter(*zip(*city_locs), c="red", s=40, label="Cities")
    plt.plot(route_x, route_y, "-o", c="blue", label="Best route")
    plt.title(f"{title} (Distance = {distance:.2f})")
    plt.legend()
    plt.show()

def plot_evolution(title : str ,evo_list : List[float]) -> None:
    plt.figure(figsize=(10, 6))
    plt.plot(evo_list, label="Path Distance", color="blue")
    plt.xlabel("Iteration")
    plt.ylabel("Path Length")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
