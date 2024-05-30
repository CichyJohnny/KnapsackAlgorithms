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

times_bf = [[] for _ in range(max_n)]
times_dp = [[] for _ in range(max_n)]
times_ga = [[] for _ in range(max_n)]

ns = range(1, max_n+1)

for num_n, n in enumerate(ns):
    for _ in range(num_tries):
        items = [(int(random()*max_w), int(random()*max_v)) for _ in range(n)]

        ga = GreedyAlgorithm()
        ga.n = n
        ga.c = max_c
        ga.items = items

        bf = BruteForce()
        bf.n = n
        bf.c = max_c
        bf.items = items

        dp = DynamicProgramming()
        dp.n = n
        dp.c = max_c
        dp.items = items

        start = perf_counter()
        ga.solve()
        times_ga[num_n].append(perf_counter() - start)

        start = perf_counter()
        bf.solve()
        times_bf[num_n].append(perf_counter() - start)

        start = perf_counter()
        dp.solve()
        times_dp[num_n].append(perf_counter() - start)


plt.figure(figsize=(10, 6))
plt.plot(ns, list(map(np.average, map(np.log, times_bf))), label='Brute Force')
plt.errorbar(ns, list(map(np.average, map(np.log, times_bf))), yerr=list(map(np.std, map(np.log, times_bf))),
             label='Brute Force', fmt='none', ecolor='black', capsize=1)
plt.plot(ns, list(map(np.average, map(np.log, times_dp))), label='Dynamic Programming')
plt.errorbar(ns, list(map(np.average, map(np.log, times_dp))), yerr=list(map(np.std, map(np.log, times_bf))),
             label='Dynamic Programming', fmt='none', ecolor='black', capsize=1)
plt.plot(ns, list(map(np.average, map(np.log, times_ga))), label='Greedy Algorithm')
plt.errorbar(ns, list(map(np.average, map(np.log, times_ga))), yerr=list(map(np.std, map(np.log, times_bf))),
             label='Greedy Algorithm', fmt='none', ecolor='black', capsize=1)

plt.title('Comparison of knapsack algorithms')
plt.xlabel('Number of items (n)')
plt.ylabel('Time of function log(s)')
plt.legend()
plt.savefig(f'figures/comparison_const_c.png')
plt.show()
