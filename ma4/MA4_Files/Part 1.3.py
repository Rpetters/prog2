"""
Solutions to module 4 1.3
Student: Rasmus Pettersson
Mail: rasmus.pettersson98@gmail.com
Reviewed by: 
Reviewed date: 2023-10-18
"""

import math
import random
import concurrent.futures
import time

def inside_hypersphere(point):
    return sum(x**2 for x in point) <= 1

def monte_carlo_simulation(n, d):
    inside_count = 0
    for _ in range(n):
        point = [random.uniform(-1, 1) for _ in range(d)]
        if inside_hypersphere(point):
            inside_count += 1
    return inside_count

def simulate_point(args):
    points_per_process, d = args
    return monte_carlo_simulation(points_per_process, d)

def parallel_monte_carlo(n, d, processes):
    points_per_process = n  #now each process handles n points
    args = [(points_per_process, d) for _ in range(processes)]

    with concurrent.futures.ProcessPoolExecutor(max_workers=processes) as executor:
        results = executor.map(simulate_point, args)
    return sum(results)

def main():
    d = 4
    n = 100000  #each process will handle 1,000,000 points
    processes = 10

    #Without parallelization
    start = time.perf_counter()
    count_single = monte_carlo_simulation(n * processes, d)  #single process handles all 10,000,000 points
    end = time.perf_counter()
    time_single = end - start

    #With parallelization
    start = time.perf_counter()
    count_parallel = parallel_monte_carlo(n, d, processes)  #total points across all processes is 10,000,000
    end = time.perf_counter()
    time_parallel = end - start

    #Calculate the volumes based on the counts
    volume_single = (count_single / (n * processes)) * (2 ** d)
    volume_parallel = (count_parallel / (n * processes)) * (2 ** d)

    print(f"Results without parallelization: Volume: {volume_single:.5f}, Execution time: {time_single:.2f} seconds")
    print(f"Results with parallelization: Volume: {volume_parallel:.5f}, Execution time: {time_parallel:.2f} seconds")

    speedup = time_single / time_parallel
    print(f"The parallelized version was {speedup:.2f} times faster.")

if __name__ == "__main__":
    main()