# Travelling-Salesman-Problem-using-Genetic-Algorithm
This repository contains a Python implementation of a genetic algorithm to solve the Travelling Salesman Problem (TSP). The code utilizes the Pygame library for visualizing the TSP solution and provides an interactive interface for the user to input the city coordinates.

## Description
The Travelling Salesman Problem is a classic optimization problem where the task is to find the shortest possible route that allows a salesman to visit a set of cities and return to the starting city, while visiting each city exactly once. The genetic algorithm approach in this code aims to find an approximate solution to the TSP.

The code prompts the user to input the number of cities and their respective coordinates through a Pygame-based graphical interface. It then uses a genetic algorithm to evolve a population of routes, iteratively improving the solutions. The best solution found, along with the corresponding shortest distance, is displayed at the end.

## Genetic Algorithms
A genetic algorithm is a search and optimization technique inspired by the process of natural selection and genetics. It is a metaheuristic approach that mimics the evolution of species in nature to find optimal or near-optimal solutions to complex problems.

In the context of the Travelling Salesman Problem (TSP), a genetic algorithm starts with an initial population of random solutions (routes). These solutions are then evaluated based on a fitness function, which in this case is the total distance of the route. The genetic algorithm iteratively applies genetic operators such as selection, crossover, and mutation to evolve new generations of routes.

## Why Genetic Algorithms for the TSP?
Genetic algorithms have several advantages when applied to the TSP:

* They can handle large problem sizes with a reasonable computational cost.
* They are capable of finding good solutions even in the absence of global information about the problem.
* They can explore different regions of the search space, increasing the chances of finding a better solution.
* They are flexible and can be easily adapted to handle variations of the TSP, such as the asymmetric TSP or the dynamic TSP.
* Due to these advantages, genetic algorithms have become a popular approach for solving the Travelling Salesman Problem and other combinatorial optimization problems.

## Dependencies
* Python 3.x
* Pygame

## How to Run
1. Clone the Repository:
```
git clone **add git link here**
```
2. Install the Dependencies
3. Run the code:
```
python app.py
```



