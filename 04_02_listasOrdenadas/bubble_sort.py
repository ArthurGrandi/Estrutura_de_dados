"""
Bubble Sort (Ordenação por Bolha): Este é um dos algoritmos de ordenação mais simples. Ele funciona percorrendo repetidamente a lista, comparando elementos adjacentes e trocando-os se estiverem na ordem errada. A passagem pela lista é repetida até que a lista esteja ordenada. É chamado de Bubble Sort porque elementos menores gradualmente "sobem" para o topo da lista.

Como funciona:

Percorra a matriz, um valor de cada vez.
Para cada valor, compare o valor com o próximo valor.
Se o valor for maior que o próximo, troque os valores para que o valor mais alto fique por último.
Percorra a matriz quantas vezes houver valores na matriz.
"""

def bubble_sort(arr):
    n = len(arr)
    # Percorre todos os elementos do array
    for i in range(n):
        # Últimos i elementos já estão ordenados, então não precisamos checá-los novamente
        for j in range(0, n-i-1):
            # Se o elemento atual for maior que o próximo elemento, troca-os
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Exemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Array ordenado:")
for i in range(len(arr)):
    print("%d" % arr[i])
