# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:32:12 2023

@author: Tarnover
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Set up the parameters for the configuration model network
N = 1000  # Number of nodes
p = 0.05  # Probability of edge creation

# Generate the degree sequence using a Poisson distribution
degrees = np.random.poisson(10, N)-1

# Create the configuration model network
G = nx.configuration_model(degrees)

# Remove self-loops and parallel edges
G = nx.Graph(G)

# Plot the degree distribution of the network
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degree_count = np.unique(degree_sequence, return_counts=True)
plt.bar(degree_count[0], degree_count[1], width=0.8, color='b')
plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
plt.show()