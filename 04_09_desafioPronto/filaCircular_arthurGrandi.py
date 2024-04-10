"""
Desafio de fila circular utilizando arrays

Elabore as funções de inserção, retirada e consulta para uma fila circular utilizando de arrays que contém 5 nodos.

Ajustar o código-fonte para gerar o falso overflow, mantendo as demais funcionalidades em perfeito funcionamento conforme o que foi discutido em aula (comportamento esperado para a fila circular).

Nome: Arthur Annes Grandi

Falso Overflow: No método "fila_inserir", se a fila está cheia, em vez de bloquear a inserção, o código simula um "falso overflow" ao avançar o ponteiro de início da fila (front) e decrementar o tamanho da fila antes de adicionar o novo elemento. Isso efetivamente sobrescreve o elemento mais antigo da fila.

Classe fila_circular: Implementa a fila circular com métodos para verificar se está cheia (fila_cheia) ou vazia (fila_vazia), inserir (fila_inserir) e remover (fila_remover) elementos, encontrar um elemento (fila_encotrar), e exibir a fila (fila_mostrar).

"""

import numpy as np

fila = [None] * 5  # Array para representar a fila circular
tamanho_fila = 5  # Tamanho da fila
rear = 0  # Variável de controle para inserção de elementos na fila (rear = traseira)
front = 0  # Variável de controle para remoção de elementos na fila (front = frente)


# FUNÇÃO PARA INSERIR NOVO ELEMENTO:
def fila_inserir(elemento):
    global rear
    global front

    espacos_vazios = 0
    for i in range(tamanho_fila):
        if fila[i] == None:
            espacos_vazios += 1

        if espacos_vazios >= 2 and rear == tamanho_fila:
            rear = 0

    if rear + 1 == front or (rear == tamanho_fila and espacos_vazios == 1):
        print(f'\n--> Falso Overflow! <--\n')

    elif rear == tamanho_fila:
        print(f'\nFila cheia --> OVERFLOW\n')

    elif rear + 1 != front:
        fila[rear] = elemento
        rear += 1

    print(f'\n{fila} Traseira:{rear} Frente:{front}\n')


# FUNÇÃO PARA REMOVER ELEMENTO
def fila_remover():
    global front
    global rear

    if rear == front:
        print('\nFila vazia --> UNDERFLOW\n')

    else:
        if front + 1 > tamanho_fila:
            front = 0

        fila[front] = None
        front += 1

    if front - 1 == rear:
        front = 0
    print(f'\n{fila} Traseira:{rear} Frente:{front}\n')


# FUNÇÃO PARA ENCONTRAR UM ELEMENTO NA FILA:
def fila_encontrar(elemento):
    encontrado = False
    for i in range(tamanho_fila):
        if fila[i] == elemento:
            encontrado = True
            print(f"\nO {elemento} está no índice {i} da fila!\n")

    if not encontrado:
        print("\nO elemento não está na fila!\n")


# MENU PARA O USUÁRIO ESCOLHER O QUE ELE QUER VERIFICAR:
while True:
    opcao = int(input('Menu:\n0- SAIR\n1- Inserir novo elemento\n2- Remover elemento\n3- Exibir fila\n4- Encontrar elemento\n\nEscolha uma das opções acima: '))

    if opcao == 0:
        break

    elif opcao == 1:
        elemento = int(input('Digite o elemento que deseja adicionar: '))
        fila_inserir(elemento)

    elif opcao == 2:
        fila_remover()

    elif opcao == 3:
        print(fila)
        print()

    elif opcao == 4:
        elemento_procurado = int(input('Digite o elemento que deseja procurar na fila: '))
        fila_encontrar(elemento_procurado)

    else:
        print('Opção inválida!')
