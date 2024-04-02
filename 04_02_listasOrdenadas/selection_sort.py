"""
Selection Sort (Ordenação por Seleção): Este algoritmo divide a lista de entrada em duas partes: uma sub-lista ordenada e uma sub-lista não ordenada. Inicialmente, a sub-lista ordenada está vazia, e a sub-lista não ordenada contém todos os elementos. O algoritmo seleciona o menor elemento da sub-lista não ordenada e o move para o final da sub-lista ordenada. Esse processo é repetido até que a sub-lista não ordenada se torne vazia.

Como funciona:

Percorra a matriz para encontrar o valor mais baixo.
Mova o valor mais baixo para a frente da parte não classificada da matriz.
Percorra a matriz novamente quantas vezes houver valores na matriz.
"""

def selection_sort(arr):
    n = len(arr)
    # Percorre todos os elementos do array
    for i in range(n):
        # Encontra o índice do menor elemento restante
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Troca o menor elemento encontrado com o primeiro elemento não ordenado
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Exemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("Array ordenado:")
for i in range(len(arr)):
    print("%d" % arr[i])
