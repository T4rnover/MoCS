import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def sis_model(u, t, beta):
    return beta * u * (1 - u)

beta = 0.1
u0 = np.random.randint(0, 2, size=1000)
t = np.linspace(0, 100, 101)
sol = odeint(sis_model, u0, t, args=(beta,))

plt.plot(t, sol)
plt.xlabel('Time')
plt.ylabel('Number of Infected Individuals')
plt.show()
