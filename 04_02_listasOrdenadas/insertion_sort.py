"""
Insertion Sort (Ordenação por Inserção): Este algoritmo funciona construindo uma parte ordenada da lista um elemento de cada vez. Ele começa com o segundo elemento na lista e o compara com os elementos anteriores, movendo cada elemento uma posição à direita até encontrar a posição correta para o elemento atual na parte ordenada. Ele repete esse processo até que toda a lista esteja ordenada.

Como funciona:

Pegue o primeiro valor da parte não classificada da matriz.
Mova o valor para o local correto na parte classificada da matriz.
Percorra a parte não classificada da matriz novamente quantas vezes houver valores.
"""

def insertion_sort(arr):
    # Percorre todos os elementos do array, começando do segundo elemento
    for i in range(1, len(arr)):
        key = arr[i]  # Elemento atual a ser inserido na parte ordenada
        j = i - 1     # Índice do último elemento na parte ordenada
        
        # Move os elementos maiores que o elemento atual para frente
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insere o elemento atual na posição correta na parte ordenada
        arr[j + 1] = key

# Exemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("Array ordenado:")
for i in range(len(arr)):
    print("%d" % arr[i])
