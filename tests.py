from BF import BruteForce
from DP import DynamicProgramming
from GA import GreedyAlgorithm

from time import perf_counter
from random import random

import matplotlib.pyplot as plt
import numpy as np

# Adjustable
max_n = 10
max_c = 100
max_w = 100
max_v = 100
num_tries = 10

times_bf = [[[] for _ in range(max_c//10)] for _ in range(max_n)]
times_dp = [[[] for _ in range(max_c//10)] for _ in range(max_n)]
times_ga = [[[] for _ in range(max_c//10)] for _ in range(max_n)]

ns = range(1, max_n+1)
cs = range(1, max_c+1, 10)

for num_n, n in enumerate(ns):
    for num_c, c in enumerate(cs):
        for _ in range(num_tries):
            items = [(int(random()*max_w), int(random()*max_v)) for _ in range(n)]

            ga = GreedyAlgorithm()
            ga.n = n
            ga.c = c
            ga.items = items

            bf = BruteForce()
            bf.n = n
            bf.c = c
            bf.items = items

            dp = DynamicProgramming()
            dp.n = n
            dp.c = c
            dp.items = items

            start = perf_counter()
            ga.solve()
            times_ga[num_n][num_c].append(perf_counter() - start)

            start = perf_counter()
            bf.solve()
            times_bf[num_n][num_c].append(perf_counter() - start)

            start = perf_counter()
            dp.solve()
            times_dp[num_n][num_c].append(perf_counter() - start)


ns_mesh, cs_mesh = np.meshgrid(ns, cs)

times_bf = np.array(times_bf)
average_times_bf = np.average(times_bf, axis=2).T
std_times_bf = np.std(times_bf, axis=2)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(cs_mesh, ns_mesh, average_times_bf, label='Brute Force', cmap='viridis')
ax.errorbar(cs_mesh.flatten(), ns_mesh.flatten(), average_times_bf.flatten(), yerr=std_times_bf.flatten(),
            fmt='|', color='black', capsize=3, label='Brute Force')

ax.set_title('Knapsack Brute Force algorithm')
ax.set_xlabel('Knapsack capacity (c)')
ax.set_ylabel('Number of items (n)')
ax.set_zlabel('Time of function (s)')

plt.savefig(f'figures/BF.png')
plt.show()


times_dp = np.array(times_dp)
average_times_dp = np.average(times_dp, axis=2).T
std_times_dp = np.std(times_dp, axis=2)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(cs_mesh, ns_mesh, average_times_dp, label='Dynamic Programming', cmap='viridis')
ax.errorbar(cs_mesh.flatten(), ns_mesh.flatten(), average_times_dp.flatten(), yerr=std_times_dp.flatten(),
            fmt='|', color='black', capsize=3, label='Brute Force')

ax.set_title('Knapsack Dynamic Programming algorithm')
ax.set_xlabel('Knapsack capacity (c)')
ax.set_ylabel('Number of items (n)')
ax.set_zlabel('Time of function (s)')

plt.savefig(f'figures/DP.png')
plt.show()

times_ga = np.array(times_ga)
average_times_ga = np.average(times_ga, axis=2).T
std_times_ga = np.std(times_ga, axis=2)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(cs_mesh, ns_mesh, average_times_ga, label='Greedy Algorithm', cmap='viridis')
ax.errorbar(cs_mesh.flatten(), ns_mesh.flatten(), average_times_ga.flatten(), yerr=std_times_ga.flatten(),
            fmt='|', color='black', capsize=3, label='Greedy Algorithm')

ax.set_title('Knapsack Greedy algorithm')
ax.set_xlabel('Knapsack capacity (c)')
ax.set_ylabel('Number of items (n)')
ax.set_zlabel('Time of function (s)')

plt.savefig(f'figures/GA.png')
plt.show()
