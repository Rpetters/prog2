"""
Solutions to module 4 1.2
Student: Rasmus Pettersson
Mail: rasmus.pettersson98@gmail.com
Reviewed by: Roman Iakymchuk
Reviewed date: 2023-10-18
"""

import random
import math
from functools import reduce

def inside_hypersphere(point):
    #Check if a point is inside the unit hypersphere
    return sum(map(lambda x: x**2, point)) <= 1  #Using map() and lambda function

def monte_carlo_volume_approximation(n, d):
    inside_count = 0

    #Generate n random points in d dimensions
    points = [[random.uniform(-1, 1) for _ in range(d)] for _ in range(n)]  #Using list comprehension

    #Filter points that are inside the hypersphere
    points_inside = filter(inside_hypersphere, points)  # Using filter()

    #Count the number of points inside the hypersphere
    inside_count = reduce(lambda acc, _: acc + 1, points_inside, 0)  #Using reduce() and lambda function

    #The volume of the hypersphere in d-dimensional space is proportional to the count of points inside
    #divided by the total number of points, scaled to the volume of the space being sampled
    volume_approximation = (inside_count / n) * (2 ** d)

    return volume_approximation

#Exact volume of a unit d-dimensional hypersphere
def exact_volume(d):
    return (math.pi ** (d / 2)) / math.gamma(d / 2 + 1)

#Test the functions with the specified parameters
n = 100000
dimensions = [2, 11]
for d in dimensions:
    approx_volume = monte_carlo_volume_approximation(n, d)
    exact_vol = exact_volume(d)

    print(f"For (n, d) = ({n}, {d}):")
    print(f"Approximate Volume: {approx_volume:.5f}")
    print(f"Exact Volume: {exact_vol:.5f}\n")