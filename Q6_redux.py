# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 08:42:21 2023

@author: Tarnover
"""

import random
import matplotlib.pyplot as plt

# Set up the grid
grid_size = (200, 200)
grid = [[0] * grid_size[1] for _ in range(grid_size[0])]
grid[grid_size[0] // 2][grid_size[1] // 2] = 1

# Set up the maximum number of particles and the current particle count
max_particles = 10000
particle_count = 0

# Set up the particle radius and the maximum step size
particle_radius = 1
max_step_size = 1

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
        if grid[new_x][new_y]:
            grid[x][y] = 1
            particle_count += 1
            break

        # Update the position
        x = new_x
        y = new_y

# Draw the particles on the screen
plt.matshow(grid, cmap='gray')
plt.show()


# Set up the grid
grid_size = (200, 200)
grid = [[0] * grid_size[1] for _ in range(grid_size[0])]
grid[grid_size[0] // 2][grid_size[1] // 2] = 1

# Set up the maximum number of particles and the current particle count
max_particles = 10000
particle_count = 0

# Set up the particle radius and the maximum step size
particle_radius = 1
max_step_size = 1

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
        if grid[new_x][new_y]:
            grid[x][y] = 1
            particle_count += 1
            break

        # Update the position
        x = new_x
        y = new_y

# Draw the particles on the screen
plt.matshow(grid, cmap='gray')
plt.show()


# Set up the grid
grid_size = (200, 200)
grid = [[0] * grid_size[1] for _ in range(grid_size[0])]
grid[grid_size[0] // 2][grid_size[1] // 2] = 1

# Set up the maximum number of particles and the current particle count
max_particles = 10000
particle_count = 0

# Set up the particle radius and the maximum step size
particle_radius = 1
max_step_size = 1

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
        if grid[new_x][new_y]:
            grid[x][y] = 1
            particle_count += 1
            break

        # Update the position
        x = new_x
        y = new_y

# Draw the particles on the screen
plt.matshow(grid, cmap='gray')
plt.show()
