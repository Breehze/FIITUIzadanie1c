import matplotlib.pyplot as plt

def plot_path(title,city_locs,path,distance):
    route_x = [city_locs[i][0] for i in path] + [city_locs[path[0]][0]]
    route_y = [city_locs[i][1] for i in path] + [city_locs[path[0]][1]]

    plt.figure(figsize=(7, 7))
    plt.scatter(*zip(*city_locs), c="red", s=40, label="Cities")
    plt.plot(route_x, route_y, "-o", c="blue", label="Best route")
    plt.title(f"{title} (Distance = {distance:.2f})")
    plt.legend()
    plt.show()

