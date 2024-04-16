"""
Merge Sort (Ordenação por Fusão): O Merge Sort é outro algoritmo de ordenação eficiente que segue a abordagem de divisão e conquista. Ele divide repetidamente a lista em metades iguais até que cada sublista contenha apenas um elemento. Em seguida, as sublistas são mescladas em pares, mantendo a ordenação, até que toda a lista seja mesclada em uma única lista ordenada.

Este código Python implementa o algoritmo Merge Sort. Ele divide a lista em duas metades recursivamente até que cada sublista contenha apenas um elemento. Em seguida, as sublistas são mescladas em pares, mantendo a ordenação, até que toda a lista seja mesclada em uma única lista ordenada.
"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Encontra o meio da lista
        left_half = arr[:mid]  # Divide a lista em duas metades
        right_half = arr[mid:]

        # Chamada recursiva para ordenar as duas metades
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge das duas metades ordenadas
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Verifica se ainda há elementos restantes em ambas as metades
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Exemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print("Array ordenado:")
print(arr)
