"""
Questão 4

Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os
demais elementos. Escreva ao final a matriz obtida.
"""

import numpy as np

matriz = np.zeros((5,5),dtype=int)

np.fill_diagonal(matriz,1)

print("matriz resultante:")
print(matriz)