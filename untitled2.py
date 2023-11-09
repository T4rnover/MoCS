import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

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
plt.ticklabel_format(style='plain')
plt.plot(t, sol[:, 0], 'b', label='P(t)')
plt.plot(t, sol[:, 1], 'g', label='Q(t)')
plt.plot(t, sol[:, 2], 'r', label='C(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

# Create a phase plot with steamplot based direction field
plt.figure()
plt.ticklabel_format(style='plain')
# Plot the trajectories of P, Q, and C in the phase space
plt.plot(sol[:, 0], sol[:, 1], 'b', label='P-Q')
plt.plot(sol[:, 0], sol[:, 2], 'g', label='P-C')
plt.plot(sol[:, 1], sol[:, 2], 'r', label='Q-C')
plt.legend(loc='best')
plt.xlabel('P')
plt.ylabel('Q or C')
plt.grid()
# Plot the vector field of the system of ODEs using streamplot function
P_range = np.linspace(0.5, 2.5)
Q_range = np.linspace(0.5, 2.5)
C_range = np.linspace(0.5, 2.5)
PP, QQ = np.meshgrid(P_range, Q_range)
dPdt, dQdt, dCdt = model([PP, QQ, C_range], None, alpha, beta, gamma)
magnitude = np.sqrt(dPdt**2 + dQdt**2 + dCdt**2)
dPdt_normed = dPdt / magnitude
dQdt_normed = dQdt / magnitude
dCdt_normed = dCdt / magnitude
plt.streamplot(PP,QQ,dPdt_normed,dQdt_normed,color=magnitude,cmap=plt.cm.jet,density=1.5)
plt.show()