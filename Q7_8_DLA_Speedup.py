# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:33:24 2023

@author: Tarnover
"""

import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import numpy as np
from scipy.stats import uniform
from scipy.stats import levy
#import cv2
#from moviepy.editor import *

# Set up the grid
#grid_size = (200, 200)
#grid = [[0] * grid_size[1] for _ in range(grid_size[0])]
#grid[grid_size[0] // 2][grid_size[1] // 2] = 1

grid_size = (200, 200)

grid = np.zeros(grid_size)
grid[grid_size[0] // 2][grid_size[1] // 2] = 1

# Set up the maximum number of particles and the current particle count
max_particles = 5000
particle_count = 0

# Set up the power-law distribution
alpha = 1.5
power_dist = lambda size: np.random.power(alpha, size=size)


# Set up the particle radius and the maximum step size
particle_radius = 1
#max_step_size = int(particle_radius * power_dist(1))
max_step_size = 1

# uniformly distributed angles
#angle = uniform.rvs( size=(max_particles), loc=.0, scale=2.*np.pi )
angle = random.uniform(0, 2 * np.pi)
r = particle_radius * power_dist(1)

# levy distributed step length
#r = levy.rvs(size=max_particles)


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
            # Generate a random step in a random direction
            r = particle_radius * power_dist(1)
            dx = random.randint(-max_step_size+int(r), max_step_size+int(r))
            dy = random.randint(-max_step_size+int(r), max_step_size+int(r))
            
            # Generate a random step length from a power-law distribution
            #step_length = int(particle_radius * power_dist(1))

            # Generate a random step in a random direction
            #step_length = levy.rvs( size=max_particles )
            #angle = uniform.rvs( size=(max_particles,), loc=.0, scale=2.*np.pi )
            #angle = random.uniform(0, 2 * np.pi)
            #dx = int(step_length * np.cos(angle))
            #dy = int(step_length * np.sin(angle))
            
            #dx = int(r * np.cos(angle))
            #dy = int(r * np.sin(angle))


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


