# -*- coding: utf-8 -*-
"""
`\
  \\,
   \\\,^,.,,.
   ,;7~((\))`;;,,
   ,(@') ;)`))\;;',
    )  . ),((  ))\;,
   /;`,,/7),)) )) )\,,      ,,,... ,
  (& )`   (,((,((;( ))\,_,,;'`    `\\,
   `"    ` ), ))),/( (            `)\,
          '1/';/;  `               ))),
           (, (     /         )    ((/,
          / \                /     ((('
         ( 6--\%  ,>     ,,,(     /'))\'
          \,\,/ ,/`----~`\   \    >,))))'
            \/ /          `--7>' /((((('
            (,9             // /'('((\\\,
             \ \,,         (/,/   '\`\\'\
              `\_)1        (_)Kk    `\`\\`\
                `\|         \Z          `\
                  `          "            `

This code generates a DLA structure and then uses the box-counting method to 
measure its fractal dimension. The box-counting process involves dividing the 
structure into boxes of different sizes and counting the number of boxes that 
contain occupied positions. It plots the number of boxes versus the box 
size on a log-log plot, and the slope of the line is the fractal dimension.

The resulting plot should show a linear relationship between the log of the 
number of boxes and the log of the box size. The slope should be 
the fractal dimension of the DLA structure. 

A fractal dimension greater than 1 indicates that the structure is fractal, 
meaning that it has self-similarity at different scales.

@author: Tarnover
"""

#Box Plot
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Set the size of the grid
size = 200

# Create a 2D array to represent the grid and set the starting position to 
# the center of the grid
grid = np.zeros((size, size), dtype=int)
x = size // 2
y = size // 2
grid[x, y] = 1

# Set the maximum number of steps to take and initialize the step counter
maxSteps = 100000
stepCount = 0

# Loop until the maximum number of steps is reached
while stepCount < maxSteps:
    # Generate a random step (-1, 0, or 1) in both x and y directions
    dx = np.random.randint(-1, 2)
    dy = np.random.randint(-1, 2)

    # If the step is 0,0, skip it
    if dx == 0 and dy == 0:
        continue

    # Calculate the new x and y positions
    newX = x + dx
    newY = y + dy

    # If the new position is outside the grid, skip it
    if newX < 0 or newX >= size or newY < 0 or newY >= size:
        continue

    # If the new position is already occupied, move halfway towards that 
    # position and mark the new position as occupied
    if grid[newX, newY] == 1:
        x = x + (dx // 2)
        y = y + (dy // 2)
        grid[x, y] = 1
    # If the new position is unoccupied, move to it
    else:
        x = newX
        y = newY

    # Increment the step counter
    stepCount += 1

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