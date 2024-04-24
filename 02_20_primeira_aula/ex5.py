"""
Questão 5

Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos são da
forma:
A[i][j] = 2*i + 7*j se i < j;
A[i][j] = 3*i^2 se i = j ;
A[i][j] = 4*i^3 + 5*j^2 + 1 se i > j.
"""

# Função para calcular os elementos da matriz de acordo com as condições fornecidas
def calcular_elemento(i, j):
    if i < j:
        return 2*i + 7*j
    elif i == j:
        return 3*i**2
    else:
        return 4*i**3 + 5*j**2 + 1

# Gerar a matriz 10x10 e calcular seus elementos
matriz = [[calcular_elemento(i, j) for j in range(10)] for i in range(10)]

# Imprimir a matriz
print("Matriz 10x10:")
for linha in matriz:
    print(linha)

"""
Neste código, definimos uma função `calcular_elemento(i, j)` que calcula o elemento da matriz de acordo com as condições fornecidas. Em seguida, utilizamos uma list comprehension aninhada para gerar a matriz 10x10, calculando cada elemento usando a função `calcular_elemento(i, j)`. Por fim, imprimimos a matriz resultante linha por linha.
"""