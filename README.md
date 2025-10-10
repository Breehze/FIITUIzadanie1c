# FIIT AI Assignment 1C

Implementation of **Genetic Algorithm** and **Simulated Annealing** to approximate a solution to the **Traveling Salesman Problem (TSP)**.

This project was developed as part of the FIIT (Faculty of Informatics and Information Technologies) AI course.  
Both algorithms are applied to find near-optimal routes in the TSP by exploring different heuristic approaches.

## Run
#### Create virtual enviroment

```bash
python -m venv ./venv
```

#### Source virtual enviorment
Linux/Mac

```bash
source ./venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

#### Run the main.py

```bash 
python main.py [flags]
```

## Command-Line Flags

| Flag | Type | Default | Description |
|------|------|----------|--------------|
| `-gat` | `bool` | `false` | Enable execution of genetic algorithm using tournament selection.  |
| `-gar` | `bool` | `false` | Enable execution of genetic algorithm using rank selection. |
| `-sa` | `bool` | `false` | Enable exectuion of simulated annealing. |
| `-m` | `str` | `swap` | Select a mutation between **swap** and **reverse** |
| `-d` | `bool` | `false` | Debug sets random.seed to 1 for city grid generation. |

### Example Usage

```bash
# Run genetic algorithm with rank and tournament selection, simulated annealing and use reverse mutation
python main.py -sa -gat -gar -m reverse

# Run genetic algorithm using tournament selection and debug mode
python main.py -gat -d
```

## Configuration
```python
"""Grid Settings"""
CITY_AMOUNT : int = 20
GRID_SIZE : int = 200

"""Simulated Annealing"""
INITIAL_TEMP : float = 1000
MINIMAL_TEMP : float = 1e-6
COOLING_RATE : float = 0.9995

"""Genetic Algorithm"""
MAX_GENERATIONS : int = 400
MUTATION_CHANCE : float = 1
POPULATION_SIZE : int = 100

TOURNAMENT_SIZE : int = 10
TOURNAMENT_AMOUNT : int = 3

WINNERS_AMOUNT : int = 30
```


This file contains adjustable parameters for the **Traveling Salesman Problem** solver using **Simulated Annealing (SA)** and a **Genetic Algorithm (GA)**.

- **Grid Settings**: Define the number of cities (`CITY_AMOUNT`) and grid size (`GRID_SIZE`).
- **Simulated Annealing**: Control temperature (`INITIAL_TEMP`, `MINIMAL_TEMP`) and cooling rate (`COOLING_RATE`).
- **Genetic Algorithm**: Set population size, number of generations, mutation chance, and tournament settings (`POPULATION_SIZE`, `MAX_GENERATIONS`, `MUTATION_CHANCE`, `TOURNAMENT_SIZE`, `TOURNAMENT_AMOUNT`, `WINNERS_AMOUNT`).

Modify these constants to tune algorithm performance and experiment with different TSP instances.


