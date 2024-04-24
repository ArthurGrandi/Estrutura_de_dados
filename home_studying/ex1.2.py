"""
1. Soma dos Números Pares: Escreva um algoritmo que recebe um número inteiro positivo N como entrada e calcula a soma de todos os números pares de 1 até N.
"""

def soma_numeros_pares(N):
    soma = 0
    for i in range(2, N+1, 2):
        soma += i
    return soma

# Solicita ao usuário que insira o valor de N
N = int(input("Digite um número inteiro positivo: "))

# Chama a função e imprime o resultado
resultado = soma_numeros_pares(N)
print("A soma dos números pares de 1 até", N, "é:", resultado)
