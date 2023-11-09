# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:11:15 2023

@author: Tarnover
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the logistic equation
def logistic(r, x):
    return r * x * (1 - x)

# Set up the parameters
num_iterations = 1000
num_points = 1000
r_min = 2.5
r_max = 4.0

# Loop over each value of r
for r in np.linspace(r_min, r_max, num_points):
    # Initialize the x value
    x = 0.5

    # Iterate the logistic equation
    for i in range(num_iterations):
        x = logistic(r, x)

        # Discard the first few iterations to allow the system to settle
        if i > num_iterations // 2:
            plt.plot(r, x, '.', color='black', markersize=0.5)

# Set the axis labels and title
plt.xlabel('r')
plt.ylabel('x')
plt.title('Bifurcation Diagram of the Logistic Equation')

# Show the plot
plt.show()