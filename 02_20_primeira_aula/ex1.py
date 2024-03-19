"""
Questão 1

Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o
produto escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os
dois conjuntos e o produto escalar, sendo que o produto escalar é dado por: x1
∗ y1 + x2 ∗ y2 + ... + xn ∗ yn.
"""

N = int(input("insira a quantidade de numeros a serem preenchidos  \n"))
X = []
Y = []
soma = 0

for i in range (N):
    X.append(int(input("insira um numero \n")))

for i in range (N):
    Y.append(int(input("insira um numero \n")))

for i in range (N):
    multi = X[i] * Y[i]
    soma += multi
    
print(X,Y,soma)