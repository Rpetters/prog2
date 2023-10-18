#!/usr/bin/env python3
from person import Person
from numba import njit
import time
from matplotlib import pyplot as plt

# Python function
def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))

# Implement the Numba version of the Fibonacci function
@njit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return fib_numba(n-1) + fib_numba(n-2)

def main():
    # Ranges for the Fibonacci numbers
    range1 = range(30, 46)  # for all methods
    range2 = range(20, 31)  # for pure Python and Numba

    # Store timings
    timings_py = []
    timings_numba = []
    timings_cpp = []

    # Warm-up Numba function
    fib_numba(1)

    # New: create just one Person object for C++ calls
    f = Person(0)  

    # Function to perform timing with repetitions
    def time_function(func, arg, repetitions=5):
        total_time = 0
        for _ in range(repetitions):
            start = time.perf_counter()
            func(arg)
            total_time += time.perf_counter() - start
        return total_time / repetitions

    # Measure timings for pure Python and Numba in range2
    for n in range2:
        timings_py.append(time_function(fib_py, n))
        timings_numba.append(time_function(fib_numba, n))

    # Measure timings for all methods in range1
    for n in range1:
        timings_numba.append(time_function(fib_numba, n))

        # Use the same Person object for C++
        f.set(n)  # set new age
        timings_cpp.append(time_function(f.fib, None))  # no argument needed for f.fib

    # Generate plots
    plt.figure()
    plt.plot(range2, timings_py, label='Python')
    plt.plot(range2, timings_numba[:len(range2)], label='Numba')  # only the first part of Numba timings
    plt.xlabel('Fibonacci number')
    plt.ylabel('Time (seconds)')
    plt.title('Execution time for Fibonacci calculations')
    plt.legend()
    plt.savefig('fibonacci_timings_range2.png')  # adjust file name as needed

    plt.figure()
    # Correcting the error here: the range for the second set of Numba timings should start from the next index after range2
    plt.plot(range1, timings_numba[len(range2):], label='Numba')  # the rest of Numba timings
    plt.plot(range1, timings_cpp, label='C++')
    plt.xlabel('Fibonacci number')
    plt.ylabel('Time (seconds)')
    plt.title('Execution time for Fibonacci calculations')
    plt.legend()
    plt.savefig('fibonacci_timings_range1.png')

    # Uncomment the below part if you want to calculate and print the Fibonacci number for n=47
    # n = 47
    # person = Person(n)
    # print("Fibonacci for n=47 (C++):", person.fib())
    # print("Fibonacci for n=47 (Numba):", fib_numba(n))

if __name__ == "__main__":
    main()
