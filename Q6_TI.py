# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:19:03 2023

@author: Shannon O'Connor and Randy Carlson

This code implements a Diffusion Limited Aggrgation
DLA is a model of particles undergoing a random walk and aggregating
together. The classic model starts with a seed somewhere in space, 
which grows when a new walker comes in contact with it 
(by being in an adjacent space).


"""

import random
import matplotlib.pyplot as plt
import numpy as np

# Set up the grid
grid_size = (200, 200)
#grid = [[0] * grid_size[1] for _ in range(grid_size[0])]
#grid[grid_size[0] // 2][grid_size[1] // 2] = 1

grid = np.zeros(grid_size)
grid[grid_size[0] // 2][grid_size[1] // 2] = 1
size = 200


# Set up the maximum number of particles and the current particle count
max_particles = 10000
particle_count = 0

# Set up the particle radius and the maximum step size
particle_radius = 1
max_step_size = 1

grids_list = []

# +


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
        # Generate a random step in a random direction
        dx = random.randint(-max_step_size, max_step_size)
        dy = random.randint(-max_step_size, max_step_size)

        # Calculate the new position
        new_x = x + dx
        new_y = y + dy

        # Check if the new position is inside the grid
        if not (0 <= new_x < grid_size[0] and 0 <= new_y < grid_size[1]):
            continue

        # Check if the new position is adjacent to the cluster
        if grid[new_x][new_y]!=0:
            grid[x][y] = particle_count+1
            particle_count += 1
            break
        
        
        
        # Update the position
        x = new_x
        y = new_y
    


# Calculate the fractal dimension using the box-counting method
box_sizes = np.arange(1, size // 2, 1)
num_boxes = []

# Loop through different box sizes and count the number of occupied boxes
for box_size in box_sizes:
    num_boxes.append(np.sum(grid[::box_size, ::box_size]))

# Plot the results on a log-log plot
plt.loglog(box_sizes, num_boxes)
plt.title('Fractal Dimension of DLA Structure')
plt.xlabel('Box Size')
plt.ylabel('Number of Boxes')
plt.show()