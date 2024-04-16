"""
Quick Sort (Ordenação Rápida): O Quick Sort é um algoritmo de ordenação eficiente e amplamente utilizado. Ele segue uma abordagem de divisão e conquista, selecionando um elemento como pivô e particionando a lista de elementos em torno do pivô, de modo que os elementos menores que o pivô fiquem à esquerda e os elementos maiores que o pivô fiquem à direita. Em seguida, o algoritmo é aplicado recursivamente às duas partições resultantes.

Este código Python implementa o algoritmo Quick Sort utilizando uma abordagem recursiva. Ele seleciona um elemento como pivô (neste caso, o primeiro elemento da lista), divide a lista em dois subconjuntos: elementos menores ou iguais ao pivô e elementos maiores que o pivô, e então chama recursivamente o algoritmo para ordenar esses subconjuntos. Finalmente, concatena os resultados ordenados dos subconjuntos menores e maiores em torno do pivô para obter a lista ordenada completa.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        # Elementos menores que o pivô
        less = [x for x in arr[1:] if x <= pivot]
        # Elementos maiores que o pivô
        greater = [x for x in arr[1:] if x > pivot]
        # Chamada recursiva para as sublistas menores e maiores
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Exemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print("Array ordenado:")
print(sorted_arr)
