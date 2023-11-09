# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:07:28 2023

@author: Tarnover
"""

import numpy as np
from scipy.integrate import odeint

# Parameters
beta = 0.3  # transmission rate
alpha = 1.0  # recovery rate
p = 1/4  # probability for geometric degree distribution
N = 1000  # total population
kmax = 10  # maximum degree
vaccination_coverage = 0.4  # 40% of the population gets vaccinated

# Degree distribution
p_k = [(1 - p) * p**k for k in range(kmax)]

# Heterogeneous mean-field SIS model differential equations
def sis_model(y, t, rho):
    S, I = y
    dSdt = -rho * beta * S * sum(p_k[k] * I[k] for k in range(kmax)) + alpha * I
    dIdt = [rho * beta * S * p_k[k] - alpha * I[k] for k in range(kmax)]
    return [dSdt] + dIdt

# Initial conditions
I0 = [10/N] * kmax  # initial fraction of infected individuals
S0 = 1 - sum(I0)  # initial fraction of susceptible individuals
y0 = [S0] + I0

# Time points
t = np.linspace(0, 200, 200)

# Solve the differential equations for different values of rho
final_infected = []
for rho in np.linspace(0, 1, 11):
    # Solve the ODEs
    y = odeint(sis_model, y0, t, args=(rho,))

    # Print the final number of infected individuals
    print(f"rho = {rho:.1f}, final number of infected individuals = {N * sum(y[-1, 1:]):.1f}")

import matplotlib.pyplot as plt

rho_values = np.linspace(0, 1, 11)
plt.plot(rho_values, final_infected)
plt.xlabel('Vaccination rate (rho)')
plt.ylabel('Final number of infected individuals')
plt.show()