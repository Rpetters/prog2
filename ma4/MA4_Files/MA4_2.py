#!/usr/bin/env python3
from person import Person
from numba import njit
import time
from matplotlib import pyplot as plt



#Python function
def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))

#Numba function
@njit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return(fib_numba(n-1) + fib_numba(n-2))

def time_functions_and_plot():
    n_values = list(range(10, 20))
    times_py = []
    times_numba = []
    times_cpp = []

    # Time the functions
    for n in n_values:
        #Python
        start = time.perf_counter()
        fib_py(n)
        end = time.perf_counter()
        times_py.append(end - start)

        #Numba
        start = time.perf_counter()
        fib_numba(n)
        end = time.perf_counter()
        times_numba.append(end - start)

        #C++
        person = Person(n)
        start = time.perf_counter()
        person.fib()
        end = time.perf_counter()
        times_cpp.append(end - start)

    #Create plots
    plt.figure()
    plt.plot(n_values, times_py, label='Python')
    plt.plot(n_values, times_numba, label='Numba')
    plt.plot(n_values, times_cpp, label='C++')
    plt.xlabel('n')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.savefig('fibonacci_timings.png')  # Save figure

    # Calculate Fibonacci number for n = 47 using C++ and Numba
    n = 47
    person = Person(n)
    print("Fibonacci for n=47 (C++):", person.fib())
    print("Fibonacci for n=47 (Numba):", fib_numba(n))

if __name__ == "__main__":
    time_functions_and_plot()