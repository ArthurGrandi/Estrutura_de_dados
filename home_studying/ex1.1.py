"""
1. Soma dos Números Pares: Escreva um algoritmo que recebe um número inteiro positivo N como entrada e calcula a soma de todos os números pares de 1 até N.
"""

# Solicita ao usuário que insira o valor de N
N = int(input("Digite um número inteiro positivo: "))

soma = 0
# Loop para percorrer os números de 1 até N
for i in range(1, N+1):
    # Verifica se o número é par
    if i % 2 == 0:
        soma += i

# Imprime o resultado
print("A soma dos números pares de 1 até", N, "é:", soma)
