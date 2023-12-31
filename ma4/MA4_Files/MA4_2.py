'''Solutions to module 4 2.2
Student: Rasmus Pettersson
Mail: rasmus.pettersson98@gmail.com
Reviewed by: Roman Iakymchuk
Reviewed date: 2023-10-18'''


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
        return fib_numba(n-1) + fib_numba(n-2)

def main():
    #warm-up
    fib_numba(1)
    f = Person(0)  

    # New: create just one Person object for C++ calls
    f = Person(0)  


    #Ranges for the Fibonacci numbers
    range1 = range(30, 46)  #for all methods
    range2 = range(20, 31)  #for python and Numba

    #Store timings
    timings_py = []
    timings_numba = []
    timings_cpp = []

    #Measure timings for python and Numba in range2
    for n in range2:
        start = time.perf_counter()
        fib_py(n)  #python
        end = time.perf_counter()
        timings_py.append(end - start)

        start = time.perf_counter()
        fib_numba(n)  #numba
        end = time.perf_counter()
        timings_numba.append(end - start)

    #Measure timings for all methods in range1
    for n in range1:
        #Numba
        start = time.perf_counter()
        fib_numba(n)
        end = time.perf_counter()
        timings_numba.append(end - start)

        #C++
        f = Person(n)  #creating a new Person object with age n
        start = time.perf_counter()
        f.fib()  #calling the fib method from the C++ library
        end = time.perf_counter()
        timings_cpp.append(end - start)

    #Generate plots
    plt.figure()
    plt.plot(range2, timings_py, label='Python')
    plt.plot(range2, timings_numba[:len(range2)], label='Numba')
    plt.xlabel('Fibonacci number')
    plt.ylabel('Time (seconds)')
    plt.title('Execution time for Fibonacci calculations')
    plt.legend()
    plt.savefig('timings_range2.png')

    plt.figure()
    plt.plot(range1, timings_numba[len(range2):], label='Numba')
    plt.plot(range1, timings_cpp, label='C++')
    plt.xlabel('Fibonacci number')
    plt.ylabel('Time (seconds)')
    plt.title('Execution time for Fibonacci calculations')
    plt.legend()
    plt.savefig('timings_range1.png')


    n = 47
    person = Person(n)
    print("Fibonacci for n=47 (C++):", person.fib())
    print("Fibonacci for n=47 (Numba):", fib_numba(n))

if __name__ == "__main__":
    main()
