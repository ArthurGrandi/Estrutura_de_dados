"""
Questão 2

Faça um programa que leia um vetor de 15 posições e o compacte, ou seja,
elimine as posições com valor zero armazenado. Para isso, todos os elementos
à frente do valor zero, devem ser movidos uma posição para trás no vetor. Ao
final exiba o vetor resultante.
"""

N = int(input("insira a quantidade de numeros a serem preenchidos  \n"))
X = []
X2 = []

for i in range (N):
    X.append(int(input("insira um numero \n")))
    if X[i] != 0:
        X2.append(X[i])
        
print(X2)