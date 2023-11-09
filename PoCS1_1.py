import numpy as np

# Define the variables and their dimensions
variables = ['V', 'N', 'L', 'W']
dimensions = {'V': 1, 'N': 0, 'L': 1, 'W': 1}

# Define the pi groups
pi_groups = {
    'pi1': {'variables': ['V', 'N', 'L'], 'powers': [1, 0, -1]},
    'pi2': {'variables': ['V', 'L', 'W'], 'powers': [1, 0, -1]},
    'pi3': {'variables': ['V', 'L'], 'powers': [1, -2]},
    'pi4': {'variables': ['P', 'V', 'N'], 'powers': [1, 0, 1]},
    'pi5': {'variables': ['N', 'L', 'W'], 'powers': [0, 0, 1]}
}

# Define the constants
constant = 1.0

# Solve for the pi groups
A = np.array([[pi['variables'].count(var) - pi['powers'][dimensions.keys().index(var[0])] for var in variables] for pi in pi_groups.values()])
b = np.zeros(len(pi_groups))
b[0] = constant
x = np.linalg.lstsq(A, b, rcond=None)[0]

# Find the dimensionless variables
dimensionless_vars = {var: var * (pi_groups['pi'+str(i+1)]['powers'][dimensions.keys().index(var[0])] / dimensions[var]) for i, var in enumerate(variables)}

# Find the dimensionless combination
dimensionless_combination = f"({dimensionless_vars['V']}) / ({dimensionless_vars['N']}^{1/9})"
print(f"The dimensionless combination is {dimensionless_combination}")
