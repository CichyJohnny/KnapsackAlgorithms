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

times_bf = [[] for _ in range(max_c//10)]
times_dp = [[] for _ in range(max_c//10)]
times_ga = [[] for _ in range(max_c//10)]

cs = range(10, max_c+1, 10)

for num_c, c in enumerate(cs):
    for _ in range(num_tries):
        items = [(int(random()*max_w), int(random()*max_v)) for _ in range(max_n)]

        ga = GreedyAlgorithm()
        ga.n = max_n
        ga.c = c
        ga.items = items

        bf = BruteForce()
        bf.n = max_n
        bf.c = c
        bf.items = items

        dp = DynamicProgramming()
        dp.n = max_n
        dp.c = c
        dp.items = items

        start = perf_counter()
        ga.solve()
        times_ga[num_c].append(perf_counter() - start)

        start = perf_counter()
        bf.solve()
        times_bf[num_c].append(perf_counter() - start)

        start = perf_counter()
        dp.solve()
        times_dp[num_c].append(perf_counter() - start)

plt.figure(figsize=(10, 6))
plt.plot(cs, list(map(np.average, times_bf)), label='Brute Force')
plt.errorbar(cs, list(map(np.average, times_bf)), yerr=list(map(np.std, times_bf)),
             label='Brute Force', fmt='none', ecolor='black', capsize=1)

plt.title('Knapsack Brute Force algorithm with constant number of items')
plt.xlabel('Knapsack capacity (c)')
plt.ylabel('Time of function (s)')
plt.legend()
plt.savefig(f'figures/BF_const_n.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(cs, list(map(np.average, times_dp)), label='Dynamic Programming')
plt.errorbar(cs, list(map(np.average, times_dp)), yerr=list(map(np.std, times_bf)),
             label='Dynamic Programming', fmt='none', ecolor='black', capsize=1)

plt.title('Knapsack Dynamic Programming algorithm with constant number of items')
plt.xlabel('Knapsack capacity (c)')
plt.ylabel('Time of function (s)')
plt.legend()
plt.savefig(f'figures/DP_const_n.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(cs, list(map(np.average, times_ga)), label='Greedy Algorithm')
plt.errorbar(cs, list(map(np.average, times_ga)), yerr=list(map(np.std, times_bf)),
             label='Greedy Algorithm', fmt='none', ecolor='black', capsize=1)

plt.title('Greedy Algorithm with constant number of items')
plt.xlabel('Knapsack capacity (c)')
plt.ylabel('Time of function (s)')
plt.legend()
plt.savefig(f'figures/GA_const_n.png')
plt.show()
