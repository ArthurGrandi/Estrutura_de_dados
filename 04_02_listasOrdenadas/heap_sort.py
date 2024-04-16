"""
Heap Sort (Ordenação por Heap): O Heap Sort é um algoritmo de ordenação baseado em uma estrutura de dados chamada heap. Ele constrói uma heap a partir dos elementos da lista e então repete a remoção do elemento máximo da heap (ou mínimo, dependendo do tipo de heap) até que todos os elementos tenham sido removidos e ordenados.

Este código Python implementa o algoritmo Heap Sort. Primeiro, ele constrói uma heap máxima a partir da lista fornecida, reorganizando os elementos. Em seguida, ele extrai elementos da heap um por um, resultando na lista ordenada.
"""

def heapify(arr, n, i):
    largest = i  # Inicializa o maior como raiz
    left = 2 * i + 1  # Índice do filho esquerdo
    right = 2 * i + 2  # Índice do filho direito

    # Verifica se o filho esquerdo da raiz existe e é maior que a raiz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Verifica se o filho direito da raiz existe e é maior que a raiz
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Troca a raiz se necessário
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Troca
        # Recursivamente faz heapify a subárvore afetada
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Constroi uma heap máxima
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrai elementos um por um da heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Troca
        heapify(arr, i, 0)

# Exemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
heap_sort(arr)
print("Array ordenado:")
print(arr)
