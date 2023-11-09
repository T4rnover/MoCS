# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:33:24 2023

@author: Shannon O'Connor and Randy Carlson

This Python program is a speed-up of Diffusion Limited Aggregation (DLA), a model of 
particle aggregation in which particles move randomly and stick to a growing 
cluster when they come into contact with it. 

Python imports the necessary libraries, including `numpy,` `random,` and 
`matplotlib,` and sets up the initial grid for the simulation. 

The simulation is set up to run until a maximum number of particles 
(`max_particles`) have been added to the cluster. The `alpha` parameter is 
used to define a power-law distribution for the step lengths of the particles,
which can help speed up the simulation by allowing the particles to cover 
more ground with longer steps. 

The `particle_radius` and `max_step_size` variables are used to define the 
size of the particles and the maximum distance they can move in a single step. 

The code generates a random value and step length for each particle using the 
`random.uniform` and `numpy.random.power` functions, respectively. These values
are used to update the particle's position in the simulation.

This code sets up the initial parameters for a DLA simulation and generates 
the random values needed to update the position of the particles 
in the simulation.
"""

import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np



grid_size = (200, 200)

grid = np.zeros(grid_size)
grid[grid_size[0] // 2][grid_size[1] // 2] = 1

# Set up the maximum number of particles and the current particle count
max_particles = 10000
particle_count = 0

# Set up the power-law distribution
alpha = 1.5
power_dist = lambda size: np.random.power(alpha, size=size)


# Set up the particle radius and the maximum step size
particle_radius = 1
max_step_size = 1

# uniformly distributed angles

angle = random.uniform(0, 2 * np.pi)
r = particle_radius * power_dist(1)


# Set up the figure and axis for the animation
fig, ax = plt.subplots()
im = ax.matshow(grid, cmap='YlGnBu')

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
            r = particle_radius * power_dist(1)
            dx = random.randint(-max_step_size+int(r), max_step_size+int(r))
            dy = random.randint(-max_step_size+int(r), max_step_size+int(r))
            

            # Calculate the new position
            new_x = x + dx
            new_y = y + dy

            # Check if the new position is inside the grid
            if not (0 <= new_x < grid_size[0] and 0 <= new_y < grid_size[1]):
                continue

            # Check if the new position is adjacent to the cluster
            if grid[new_x][new_y] != 0:
                grid[x][y] = 1
                particle_count += 1
                break

            # Update the position
            x = new_x
            y = new_y

    # Update the plot with the new grid
    im.set_data(grid)
    return [im]

# Set up the animation
ani = FuncAnimation(fig, update, frames=range(100), blit=True)
ani.save('DLAVideo.mp4')

# Show the animation
plt.show()


