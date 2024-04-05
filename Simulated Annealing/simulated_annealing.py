import pandas as pd
import numpy as np
import random
import math

"""We will implement a Simulated Annealing algorithm that will calculate the optimal path from city i to city j.
In the data an entry represents the distance from a city (row) to a city (column). 

This algorithm is designed to accept a starting city if a designated one is required, or to start at a random city.
"""

def get_total_distance(current_path, distances_array):
    """Calculate total distance traveled for given route. Adds distances on dataframe""" 
    distance = 0
    for i in range(len(current_path)):
        distance += distances_array[current_path[i-1], current_path[i]] # Get distance between two cities
    return distance

def swap_cities(solution, start_city=None):
    """Swaps two adjacent cities in the route."""
    # Pick a random city/index to swap with its neighbor
    # If start city designated then it will not include it in the swap
    if start_city is not None:
        index = random.randint(2, len(solution) - 1) # Excludes the first index from swapping
    else:
        index = random.randint(1, len(solution) - 1)  # Includes the first index in swaps
    new_solution = solution.copy()
    new_solution[index - 1], new_solution[index] = new_solution[index], new_solution[index - 1] # Swap cities
    return new_solution

def simulated_annealing(distances_df, start_city=None):
    """Perform simulated annealing to find a solution for the TSP."""

    # Initial path which is randomly guessed
    current_path = list(range(distances_df.shape[1])) # List of all cities
    random.shuffle(current_path) # Set random city order
    
    # If required to start at a city, we must make sure the city is first in the list
    if start_city is not None:
        current_path.remove(start_city)
        current_path = [start_city] + current_path # Add start city to beginning of list

    # Calculate the distance of the initial path/Get starting solution
    current_distance = get_total_distance(current_path, distances_df)
    best_path, best_distance = current_path, current_distance
    
    current_temp = 1000 # Initial temperature
    min_temp = 1  
    cooling_rate = 0.01   # (Alpha)

    # Begin cooling process
    while current_temp > min_temp:
        i = 0
        while i < 200: # Number of iterations at each temperature
            new_path = swap_cities(current_path.copy(), start_city=start_city) # Get random neighboring solution
            new_distance = get_total_distance(new_path, distances_df)

            # Check acceptance probability
            ap = math.exp((current_distance - new_distance) / current_temp)
            if (new_distance < current_distance) or (random.uniform(0,1) < ap):
                current_path, current_distance = new_path, new_distance
                if new_distance < best_distance:
                    best_path, best_distance = new_path, new_distance
            i += 1
        current_temp -= cooling_rate # Decrease temperature
    return best_path, best_distance

if __name__ == "__main__":
    # Load data. I had to manually delete some rows that were loading as null for some reason.
    tsp_data = pd.read_csv("tsp_data.csv", header=None, keep_default_na=False)
    tsp_data = tsp_data.to_numpy()    
    print("TSP data:")
    print(tsp_data)

    # start_city = the number of the city you want to start at. If None, it will start at a random city
    best_path, best_distance = simulated_annealing(tsp_data, start_city=None)
    print("Best path:", best_path)
    print("Best distance:", best_distance)