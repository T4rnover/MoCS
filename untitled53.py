# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 23:00:27 2023

@author: Tarnover
"""

import numpy as np

# Parameters
N = 1000
kmax = 10
beta = 0.1
gamma = 0.05

# Initialize susceptible and infected populations
S = 1.0 - 10.0/N
I = np.full(kmax, 10.0/N)

# Time step
dt = 0.01

# Euler method
for i in range(1, 20001):
    t = i*dt
    S = S - dt * (beta * S * np.sum(I) - gamma * I)
    for k in range(kmax):
        I[k] = I[k] + dt * (beta * S[k] - gamma * I[k])

# Print final susceptible and infected populations
print('Final susceptible population:', S)
print('Final infected populations:', I)