import numpy as np

# Define the variables and their dimensions
variables = ['T', 'L', 'M', 'g']
dimensions = {'T': 1, 'L': 1, 'M': 0, 'g': -1}

# Define the matrix A
A = np.array([[1, 0, 1, 0],
              [0, 1, 0, 0],
              [0, 0, -2, 1]])

# Solve for the null space of A
U, s, V = np.linalg.svd(A)
null_space = V[-1,:]

# Find the basis null vectors
basis_vectors = []
for i, var in enumerate(variables):
    basis_vector = {}
    basis_vector[var] = null_space[i]
    basis_vectors.append(basis_vector)

# Find the dimensionless variables
dimensionless_vars = []
for basis_vector in basis_vectors:
    dimensionless_var = {}
    for var in variables:
        if basis_vector.get(var, 0) != 0:
            dimensionless_var[var] = basis_vector[var] * dimensions[var]
    dimensionless_vars.append(dimensionless_var)

# Find the dimensionless combination
dimensionless_combination = {var: f"({var}/{dimensions[var]})^{dimensions[var]}" for var in variables if dimensions[var] != 0}
dimensionless_combination_str = ' * '.join([dimensionless_combination[var] for var in dimensionless_combination])
print(f"The dimensionless combination is {dimensionless_combination_str}")