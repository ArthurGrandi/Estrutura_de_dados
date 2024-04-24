"""
Questão 6

Faça um programa que permita ao usuário entrar com uma matriz de 3 x 3
números inteiros. Em seguida, gere um array unidimensional pela soma dos
números de cada coluna da matriz e mostrar na tela esse array. Por exemplo, a
matriz:

5 -8 10
1 2 15
25 10 7

Vai gerar um vetor, onde cada posição é a soma das colunas da matriz. A
primeira posição será 5 + 1 + 25, e assim por diante:
31 4 32
"""

# Solicita ao usuário que insira os elementos da matriz
print("Digite os elementos da matriz 3x3:")
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        elemento = int(input("Digite o elemento da posição ({}, {}): ".format(i+1, j+1)))
        linha.append(elemento)
    matriz.append(linha)

# Calcula a soma das colunas da matriz
soma_colunas = []
for j in range(3):
    soma = 0
    for i in range(3):
        soma += matriz[i][j]
    soma_colunas.append(soma)

# Imprime o vetor com as somas das colunas
print("Array unidimensional gerado pela soma das colunas da matriz:")
print(soma_colunas)

"""
Neste código, utilizamos dois loops for aninhados para solicitar ao usuário que insira os elementos da matriz 3x3. Em seguida, calculamos a soma dos números de cada coluna da matriz utilizando outro conjunto de loops for aninhados. Os resultados são armazenados em um vetor `soma_colunas`, que é então impresso na tela.
"""