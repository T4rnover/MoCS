import random
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation
from IPython.display import HTML
from matplotlib.animation import PillowWriter
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

# Set up the grid
grid_size = (200, 200)

grid = np.zeros(grid_size)
grid[grid_size[0] // 2][grid_size[1] // 2] = 1

max_particles = 10000
particle_count = 0

particle_radius = 1
max_step_size = 1

# Set up the power-law distribution
alpha = 1.5
power_dist = lambda size: np.random.power(alpha, size=size)

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
            # Generate a random step length from a power-law distribution
            step_length = int(particle_radius * power_dist(1))

            # Generate a random step in a random direction
            angle = random.uniform(0, 2 * np.pi)
            dx = int(step_length * np.cos(angle))
            dy = int(step_length * np.sin(angle))

            # Update the particle position
            x += dx
            y += dy

            # Check if the particle is inside the grid
            if x < 0 or x >= grid_size[0] or y < 0 or y >= grid_size[1]:
                break

            # Check if the particle is adjacent to the cluster
            if grid[x][y] == 1:
                grid[x][y] = 2
                particle_count += 1
                break



            # Update the position
            x = new_x
            y = new_y

        im = plt.imshow(grid, vmin=0, vmax=2, cmap='RdPu', animated=True)
        return [im]

 
    
# Set up the animation
ani = FuncAnimation(fig, update, frames=range(100), blit=True)
ani.save('DLAVideo.mp4')

# Show the animation
plt.show()
