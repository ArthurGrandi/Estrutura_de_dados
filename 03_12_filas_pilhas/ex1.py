"""
Em Python, as pilhas (stacks) são estruturas de dados do tipo LIFO (Last In, First Out), o que significa que o último elemento inserido é o primeiro a ser removido. As operações básicas em uma pilha são a criação, inclusão (ou empilhamento), consulta e retirada (ou desempilhamento) de elementos. Aqui estão os algoritmos básicos para cada uma dessas operações em Python:
"""
### Para adaptar a estrutura do código para trabalhar com pilhas, podemos modificar as funções e a lógica de operação. Aqui está uma versão modificada do código que usa a estrutura de pilha:

def criar_pilha():
    return []

def empilhar_elemento(pilha, elemento):
    pilha.append(elemento)

def desempilhar_elemento(pilha):
    if pilha:
        return pilha.pop()
    else:
        print("A pilha está vazia.")

def consultar_topo(pilha):
    if pilha:
        return pilha[-1]
    else:
        print("A pilha está vazia.")

def tamanho_da_pilha(pilha):
    return len(pilha)

def inserir_na_posicao(pilha, posicao, elemento):
    pilha.insert(posicao, elemento)

def exibir_menu():
    print("\nMenu:")
    Traco("1. Criar pilha")
    Traco("2. Empilhar elemento")
    Traco("3. Desempilhar elemento")
    Traco("4. Consultar elemento no topo")
    Traco("5. Determinar tamanho da pilha")
    Traco("0. Sair")

def Traco(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

pilha = []
opcao = None

while opcao != 0:
    exibir_menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        pilha = criar_pilha()
        print("Pilha criada.")
    elif opcao == 2:
        elemento = int(input("Insira o elemento que deseja empilhar: "))
        empilhar_elemento(pilha, elemento)
        print("Elemento empilhado com sucesso.")
    elif opcao == 3:
        elemento_desempilhado = desempilhar_elemento(pilha)
        if elemento_desempilhado is not None:
            print("Elemento desempilhado:", elemento_desempilhado)
    elif opcao == 4:
        topo = consultar_topo(pilha)
        if topo is not None:
            print("Elemento no topo da pilha:", topo)
    elif opcao == 5:
        tamanho = tamanho_da_pilha(pilha)
        print("Tamanho da pilha:", tamanho)
    elif opcao == 0:
        print("Encerrando o programa...")
    else:
        print("Opção inválida. Tente novamente.")

### Nessa versão modificada, as funções foram adaptadas para trabalhar com pilhas. Agora, o programa oferece opções para criar uma pilha, empilhar um elemento, desempilhar um elemento, consultar o elemento no topo da pilha e determinar o tamanho da pilha. O funcionamento geral do menu e do loop principal permanece o mesmo.

### Esses são algoritmos básicos para operações em uma pilha em Python. Eles são implementados usando listas, que são estruturas de dados dinâmicas e flexíveis em Python.
