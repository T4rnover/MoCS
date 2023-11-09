# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:34:29 2023

@author: Tarnover
"""

import networkx as nx
import EoN
import matplotlib.pyplot as plt

# Parameters for the SIS model
beta = 0.001  # infection rate
gamma = 0.1  # recovery rate

# Configuration model network parameters
N = 1000  # number of nodes
degree_sequence = [10]*N  # each node has degree 10

# Create a configuration model network
G = nx.configuration_model(degree_sequence)

# Run the SIS model
t, S, I = EoN.fast_SIS(G, beta, gamma, rho=0.1)

# Plot the results
plt.plot(t, S, label='Susceptible')
plt.plot(t, I, label='Infected')
plt.xlabel('Time')
plt.ylabel('Number of nodes')
plt.legend()
plt.show()