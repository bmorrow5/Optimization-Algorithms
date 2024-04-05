This program is a simulated annealing optimization algorithm designed to find an optimal route between two cities (traveling salesperson problem). Simulated annealing is a metaheuristic, and gives us an approximate solution to the objective function of our optimization problem. 





Hyperparameters:
Current Temperature = 1000
Minimum Temperature = 1
Cooling Rate = 0.01
Iterations per Temperature = 200

The current temperature, minimum temperature, cooling rate, and iterations per temperature are hyperparameters that can be tuned. These hyperparameters simulate the colling process of metals, and have much more of an impact on performance than I initially expected when I built the algorithm. If the cooling rate is too high, then the algorithm will not have enough time to escape local optima. If the cooling rate is too low, then the algorithm will take too long to converge. The same can be said for the other parameters if we shift them to either side and narrow the cooling time or change the cooling rate.
