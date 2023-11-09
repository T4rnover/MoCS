# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:10:23 2023

@author: Tarnover
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 08:42:21 2023

@author: Tarnover
"""

import random
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation
from IPython.display import HTML
from matplotlib.animation import PillowWriter

# Set up the grid
grid_size = (200, 200)

grid = np.zeros(grid_size)
grid[grid_size[0] // 2][grid_size[1] // 2] = 1

max_particles = 10000
particle_count = 0

particle_radius = 1
max_step_size = 1

def animate_func(i):

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


            grid[x][y]=10003

            # Calculate the new position
            new_x = x + dx
            new_y = y + dy

            #this will make it show up hopefully



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

        im = plt.imshow(grid, vmin=0, vmax=2, cmap='RdPu', animated=True)
        return [im]

 

    
fig = plt.figure( figsize=(8,8) )

 

anim = animation.FuncAnimation(
                               fig, 
                               animate_func,
                               interval=20, 
                               blit=True, 
                               save_count=2000
                               )

 

 