# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:11:31 2023

@author: Tarnover
"""

import random
import matplotlib.pyplot as plt
import numpy as np


# Set up the grid
grid_size = (200, 200)

grid = np.zeros(grid_size, dtype=bool)
grid[grid_size[0] // 2][grid_size[1] // 2] = True

max_particles = 10000
particle_count = 0

max_step_size = 1

# Set up the power-law distribution
alpha = 1.5
power_dist = lambda size: np.random.power(alpha, size=size)

# Set up the figure and axis for the animation
fig, ax = plt.subplots()
im = ax.matshow(grid, cmap='inferno')

# Define the update function for the animation
def update(frame):
    global particle_count

    # Loop until the maximum number of particles is reached
    while particle_count < max_particles:
        # Generate a random position on the edge of the grid
        if random.random() < 0.5:
            x = random.randint(0, grid_size[0] - 1)
            y = random.choice([0, grid_size[1] - 1])
        else:
            x = random.choice([0, grid_size[0] - 1])
            y = random.randint(0, grid_size[1] - 1)

        # Loop until the particle hits the cluster
        while True:
            # Generate a random step length from a power-law distribution
            step_length = int(max_step_size * power_dist(1))

            # Generate a random step in a random direction
            angle = random.uniform(0, 2 * np.pi)
            dx = int(step_length * np.cos(angle))
            dy = int(step_length * np.sin(angle))

            # Calculate the new position
            new_x = x + dx
            new_y = y + dy

            # Check if the new position is inside the grid
            if not (0 <= new_x < grid_size[0] and 0 <= new_y < grid_size[1]):
                continue

            # Check if the new position is adjacent to the cluster
            if grid[new_x][new_y]:
                grid[x][y] = True
                particle_count += 1
                break

            # Update the position
            x = new_x
            y = new_y

    # Update the plot with the new grid
    im.set_data(grid)