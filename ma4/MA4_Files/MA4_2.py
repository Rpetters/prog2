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

    # Measure timings for pure Python and Numba in range2
    for n in range2:
        start = time.perf_counter()
        fib_py(n)  # assuming fib_py is your pure Python Fibonacci function
        end = time.perf_counter()
        timings_py.append(end - start)

        start = time.perf_counter()
        fib_numba(n)
        end = time.perf_counter()
        timings_numba.append(end - start)

    # Measure timings for all methods in range1
    for n in range1:
        # Numba
        start = time.perf_counter()
        fib_numba(n)
        end = time.perf_counter()
        timings_numba.append(end - start)

        # C++
        f = Person(n)
        start = time.perf_counter()
        f.fib()
        end = time.perf_counter()
        timings_cpp.append(end - start)

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
