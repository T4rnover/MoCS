# -*- coding: utf-8 -*-
"""
                \||/
                |  @___oo
      /\  /\   / (__,,,,|
     ) /^\) ^\/ _)
     )   /^\/   _)
     )   _ /  / _)
 /\  )/\/ ||  | )_)
<  >      |(,,) )__)
 ||      /    \)___)\
 | \____(      )___) )___
  \______(_______;;; __;;;
          
          
Created on Fri Oct 13 21:07:17 2023
Generates a diffusion-limited aggregation (DLA) pattern on a 2D grid. 
It starts at the center of the grid and takes random steps until it reaches 
the edge of the grid or collides with an occupied position. If it collides 
with an occupied position, it moves halfway towards that position and marks 
the new position as occupied. The process continues until a maximum number 
of steps is reached. Finally, the occupied positions are printed as "*" 
and unoccupied positions are printed as " ".

"""
# Get our Libs
import numpy as np
import random

size = 200
# creates a 2D array of zeros
grid = np.zeros((size, size), dtype=int)

# sets the starting position to the center of the grid
x = size // 2
y = size // 2

# marks the starting position as occupied
grid[x, y] = 1

#Sets the maximum number of steps to take and initializes the step counter.
maxSteps = 100000
stepCount = 0

#Loops until the maximum number of steps is reached
while stepCount < maxSteps:
    r = np.random.power(2) * size // 2  #generates a random step length from a 
                                        #power-law distribution and a random 
                                        #angle.  This technique is pretty 
                                        #common from examples out there.
    theta = random.uniform(0, 2 * np.pi)
    
# Converts the polar coordinates to Cartesian coordinates
    dx = int(r * np.cos(theta))
    dy = int(r * np.sin(theta))

    if dx == 0 and dy == 0:   #Skips if dx,dy are 0,0
        continue

    newX = x + dx             #Updates the new position
    newY = y + dy

    if newX < 0 or newX >= size or newY < 0 or newY >= size:
        continue    #Check if we wanderd outside the grid

    if grid[newX, newY] == 1:       #Check if the new position is occupied. 
                                    
                                    
        x = x + (dx // 2)           #If so, move halfway to the position 
        y = y + (dy // 2)  
        grid[x, y] = 1              #mark the new position as occupied (1).
    else:
        x = newX                    #Check if new position is unoccupied.
        y = newY                    #If so, move to it

    stepCount += 1

#Loop rints a "*" if the position is occupied, " " otherwise.

for i in range(size):
    for j in range(size):
        print("*" if grid[i, j] == 1 else " ", end="")
    print()