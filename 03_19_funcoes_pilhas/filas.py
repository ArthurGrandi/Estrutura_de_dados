from collections import deque

d = deque()
TAM = 5

#Insere um novo elemento na fila de dados.
def NovoElemento():
    x = int(input("Digite um elemento para a fila:  "))
    if len(d) < TAM:
        d.append(x)
        print("Elemento incluido com sucesso!")
    else:
        print("Elemento não poderá ser inserido! Overflow!")

#Apaga um elemento na fila de dados.
def ApagaElemento():
    x = d.popleft()
    print(f"Elemento {x} excluido com sucesso!")

#Consulta se um elemento está na fila.
def ConsultaElemento(a:int):
    try:
        x = d.index(a)
        print(f"Elemento {a} encontrado na posiçâo: {x}")
    except:
        print(f"Elemento {a} não encontrado")
    
    
while True:
    Opcao = 0
    print (" 0 - SAIR\n 1 - Novo \n 2 - Exibe os elemento da fila \n 3 - Remove elemento da fila\n 4 - Encontra elemento na fila\n")
    Opcao = (input("Escolha uma Opção:  "))

    if Opcao == "0":
        break
    elif Opcao == "1": 
        NovoElemento()
    elif Opcao == "2": 
        print (d)
        print()
    elif Opcao == "3":
        if len(d) == 0:
             print ("Underflow.... Fila Vazia\n")
        else:
            ApagaElemento()
            print()
            print (d)
            print()
    elif Opcao == "4":
        procura = int(input("Informe o elemento que deseja verificar se está na fila:  "))
        ConsultaElemento(procura)        
    else:
        print("Esta não é uma opção válida")
        print()