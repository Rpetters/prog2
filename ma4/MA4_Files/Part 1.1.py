"""
Solutions to module 4 1.1
Student: Rasmus Pettersson
Mail: rasmus.pettersson98@gmail.com
Reviewed by: 
Reviewed date: 2023-10-18
""" 


import random
import matplotlib.pyplot as plt
import math

def calculate_pi(n):
    inside_circle = 0
    points_inside_x = []
    points_inside_y = []
    points_outside_x = []
    points_outside_y = []

    #Generate n random points and check if they are inside the circle
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
            points_inside_x.append(x)
            points_inside_y.append(y)
        else:
            points_outside_x.append(x)
            points_outside_y.append(y)

    #Calculate the approximation of pi
    pi_approx = 4 * inside_circle / n

    #Print the results
    print(f"For n = {n}:")
    print(f"Number of points inside the circle: {inside_circle}")
    print(f"Approximation of π: {pi_approx:.5f}")


    return pi_approx, points_inside_x, points_inside_y, points_outside_x, points_outside_y, inside_circle

def visualize_points(points_inside_x, points_inside_y, points_outside_x, points_outside_y, n, pi_approx):
    #Create a scatter plot of the points
    plt.figure(figsize=(8, 8))
    plt.scatter(points_inside_x, points_inside_y, color='red', s=1)  # points inside circle are red
    plt.scatter(points_outside_x, points_outside_y, color='blue', s=1)  # points outside circle are blue

    #Draw the circle
    circle = plt.Circle((0, 0), 1, color='green', fill=False)
    plt.gca().add_patch(circle)

    #Set equal aspect ratio to ensure the circle isn't distorted
    plt.gca().set_aspect('equal', adjustable='box')

    plt.title(f"Approximation of π with {n} random points: π ≈ {pi_approx:.5f}")
    plt.xlabel("x")
    plt.ylabel("y")

    #Save the figure
    filename = f"monte_carlo_pi_{n}_points.png"
    plt.savefig(filename, format='png')
    plt.close()  # Close the figure to release memory

    return filename  #Return the filename for reference

#Test the functions with different values of n
ns = [1000, 10000, 100000]
for n in ns:
    pi_approx, points_inside_x, points_inside_y, points_outside_x, points_outside_y, inside_circle = calculate_pi(n)
    filename = visualize_points(points_inside_x, points_inside_y, points_outside_x, points_outside_y, n, pi_approx)
    print(f"Saved PNG file for n = {n} as {filename}\n")