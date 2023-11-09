import numpy as np

# Define the variables and their dimensions
variables = ['E', 'rho', 'R', 't']
dimensions = {'L': 1, 'T': -2, 'M': 1}

# Define the pi groups
pi_groups = {
    'pi1': {'E': 1, 'rho': 0, 'R': 0, 't': 0},
    'pi2': {'E': 0, 'rho': 1, 'R': 0, 't': 0},
    'pi3': {'E': 0, 'rho': 0, 'R': 1, 't': 0},
    'pi4': {'E': 0, 'rho': 0, 'R': 0, 't': 1},
    'pi5': {'pi1': 0, 'pi2': 0, 'pi3': 0, 'pi4': 0}
}

# Define the constants
constant = 1.0

# Solve for the pi groups
A = np.array([[pi_groups[pi].get(var, 0) - dimensions.get(var[0], 0) for var in variables] for pi in pi_groups])
b = np.zeros(len(pi_groups))
b[0] = constant
x = np.linalg.lstsq(A, b, rcond=None)[0]

# Print the result
print(f"E = {constant:.2f} * rho^{x[0]:.2f} * R^{x[1]:.2f} * t^{x[2]:.2f}")
