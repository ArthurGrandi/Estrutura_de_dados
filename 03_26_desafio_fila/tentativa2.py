"""
Desafio de fila circular utilizando arrays

Elabore as funções de inserção, retirada e consulta para uma fila circular utilizando de arrays que contém 5 nodos.

Ajustar o código-fonte para gerar o falso overflow, mantendo as demais funcionalidades em perfeito funcionamento conforme o que foi discutido em aula (comportamento esperado para a fila circular).

Nome: Arthur Annes Grandi

Falso Overflow: No método "fila_inserir", se a fila está cheia, em vez de bloquear a inserção, o código simula um "falso overflow" ao avançar o ponteiro de início da fila (front) e decrementar o tamanho da fila antes de adicionar o novo elemento. Isso efetivamente sobrescreve o elemento mais antigo da fila.

Classe fila_circular: Implementa a fila circular com métodos para verificar se está cheia (fila_cheia) ou vazia (fila_vazia), inserir (fila_inserir) e remover (fila_remover) elementos, encontrar um elemento (fila_encotrar), e exibir a fila (fila_mostrar).

"""

import numpy as np

array = [None] * 5 #Criar um array de 5 posições e preenchê-lo com um espaço vazio
tam_array = 5 #Tamanho do array
re = 0 #Inicializando a variável r para controle de inserção de elementos no array (r = ré)
frente = 0 #Inicializando a variável f para controle de remoção de elementos no array (f = frente)


# FUNÇÃO PARA INSERIR NOVO ELEMENTO:
# Primeiro verificar as condições, antes de inserir um novo elemento.
def inserir(elemento): 
    global re
    global frente

    # Verificando se tem 2 ou mais espaços vazios para circular, e a ré voltar a posição 0 
    espaco = 0
    for i in range(tam_array):
        if array[i] == None:
            espaco = espaco +  1

        if espaco >= 2 and re == tam_array:
            re = 0

    # Condição de fila vazia 
    #if re == frente: 
        #re = 0
        #frente = 0

    # Condição para sinalizar um falso overflow, e não inserir.
    if re + 1 == frente or (re == tam_array and espaco == 1): 
        print(f'\n--> Falso Overflow! <--\n') 

    #Condição de fila cheia
    elif re == tam_array: 
            print(f'\nFila cheia --> OVERFLOW\n')

    #Condição para inserir o elemento
    elif re + 1 != frente:
        array[re] = elemento
        re = re + 1
    
    print(f'\n{array} Ré:{re} Frente:{frente}\n') 


# FUNÇÃO PARA REMOVER ELEMENTO
def remover():
    global frente
    global re
    
    if re == frente:
        print('\nFila vazia --> UNDERFLOW\n')

    else:
        if frente + 1 > tam_array:
            frente = 0

        array[frente] = None
        frente = frente + 1

    if  frente - 1 == re:
        frente = 0
    print(f'\n{array} Ré:{re} Frente:{frente}\n') 
    

# FUNÇÃO PARA ENCONTRAR UM ELEMENTO NO ARRAY:
def encontrar(array, elemento):
    procura = True #Procura vai ser true até ser encontrada no array
    for i in range(tam_array):
        if array[i] == elemento:
            procura = False
            print(f"\nO {elemento} está no índice {i} do array!\n")
        
    if procura:
        print("\nO elemento não está no ARRAY!\n") 


# MENU PARA O USUÁRIO ESCOLHER O QUE ELE QUER VERIFICAR:
while True:
    opcao = int(input('Menu:\n0- SAIR\n1- Inserir novo elemento\n2- Remover elemento\n3- Exibir elemento\n4- Encontrar elemento\n\nEscolha uma das opções acima: '))

    if opcao == 0:
        break

    elif opcao == 1: #Inserir novo elemento 
        elemento = int(input('Digite o elemento que quer adicionar: '))
        inserir(elemento)

    elif opcao == 2: #Remover elemento
        remover()

    elif opcao == 3: #Exibir os elementos 
        print(array)
        print()

    elif opcao == 4: #Procurar elemento
        procura = int(input('Digite o elemento que você quer procurar no array: '))
        encontrar(array, procura)

    else:
        print('Esta não é uma opção válida!')