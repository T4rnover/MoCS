# -*- coding: utf-8 -*-
"""
A simplified model of cartel economics. 
In this model, we use differential equations to describe how the 
price, quantity, and cost of a product interact in a cartel.

P(t) is the price of the product at time t.
Q(t) is the quantity of the product produced by the cartel at time t.
C(t) is the cost of producing the product at time t.

dP/dt = α(P - C)
dQ/dt = β(P - C)
dC/dt = γC

α, β, and γ are parameters that represent the speed at which the price, 
quantity, and cost change in response to the difference between the 
price and the cost.

***
"""

import numpy as np
from scipy.integrate import odeint

def model(y, t, alpha, beta, gamma):
    P, Q, C = y
    dPdt = alpha * (P - C)
    dQdt = beta * (P - C)
    dCdt = gamma * C
    return [dPdt, dQdt, dCdt]

# Initial conditions
y0 = [1.0, 1.0, 1.0]

# Time points
t = np.linspace(0, 10)

# Parameters
alpha = 1.5
beta = 1.3
gamma = 1.5

# Solve ODEs
sol = odeint(model, y0, t, args=(alpha, beta, gamma))

# Plot results
import matplotlib.pyplot as plt
plt.ticklabel_format(style='plain')
plt.plot(t, sol[:, 0], 'b', label='P(t)')
plt.plot(t, sol[:, 1], 'g', label='Q(t)')
plt.plot(t, sol[:, 2], 'r', label='C(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
U = np.cos(X)
V = np.sin(Y)

fig1, ax1 = plt.subplots()
ax1.set_title('Arrows scale with plot width, not view')
Q = ax1.quiver(X, Y, U, V, units='width')
qk = ax1.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
