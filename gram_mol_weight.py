# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 09:08:36 2023

@author: Tarnover
"""

atomic_weights = {'H': 1.00794, 'C': 12.0107}
hydrocarbon = 'C2H6'
molecular_weight = 0

for i, char in enumerate(hydrocarbon):
    if char.isalpha():
        element = char
        num_atoms = int(hydrocarbon[i+1:i+2]) if i < len(hydrocarbon) - 1 and hydrocarbon[i+1:i+2].isdigit() else 1
        molecular_weight += atomic_weights.get(element, 0) * num_atoms

print(f"The molecular weight of {hydrocarbon} is {round(molecular_weight, 2)} g/mol")
