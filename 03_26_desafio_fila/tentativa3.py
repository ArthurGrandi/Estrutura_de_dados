"""
Desafio de fila circular utilizando arrays

Elabore as funções de inserção, retirada e consulta para uma fila circular utilizando de arrays que contém 5 nodos.

Ajustar o código-fonte para gerar o falso overflow, mantendo as demais funcionalidades em perfeito funcionamento conforme o que foi discutido em aula (comportamento esperado para a fila circular).

Nome: Arthur Annes Grandi

Falso Overflow: No método "fila_inserir", se a fila está cheia, em vez de bloquear a inserção, o código simula um "falso overflow" ao avançar o ponteiro de início da fila (front) e decrementar o tamanho da fila antes de adicionar o novo elemento. Isso efetivamente sobrescreve o elemento mais antigo da fila.

Classe fila_circular: Implementa a fila circular com métodos para verificar se está cheia (fila_cheia) ou vazia (fila_vazia), inserir (fila_inserir) e remover (fila_remover) elementos, encontrar um elemento (fila_encotrar), e exibir a fila (fila_mostrar).

"""

# Implementa a fila circular
class fila_circular:
    def _init_(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = self.size = 0
        self.rear = capacity - 1

    # Método para verificar se está cheia
    def fila_cheia(self):
        return self.size == self.capacity

    # Método para verificar se está vazia
    def fila_vazia(self):
        return self.size == 0

    # Método para inserir um elemento
    def fila_inserir(self, item):
        if self.fila_cheia():
            print("Falso overflow. A fila está cheia, mas tentaremos sobrescrever um elemento.")
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        print(f"{item} inserido na fila.")

    # Método para remover um elemento
    def fila_remover(self):
        if self.fila_vazia():
            print("A fila está vazia.")
            return
        print(f"Removendo {self.queue[self.front]}")
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

    # Método para encontrar um elemento
    def fila_encontrar(self, item):
        for i in range(self.size):
            index = (self.front + i) % self.capacity
            if self.queue[index] == item:
                print(f"elemento {item} encontrado na posição {index}.")
                return True
        print(f"elemento {item} não encontrado.")
        return False

    # Método para apresentar no display
    def fila_mostrar(self):
        if self.fila_vazia():
            print("A fila está vazia.")
            return
        print("                      ")
        print("Fila: ", end="")
        for i in range(self.size):
            print(self.queue[(self.front + i) % self.capacity], end=" ")
        print()

# Menu interativo para o usuário
def menu_principal():
    capacity = int(input("Informe a capacidade da fila circular: "))
    q = fila_circular(capacity)

    while True:
        print("\n--- Menu Fila Circular ---")
        print("1. Inserir elemento")
        print("2. Remover elemento")
        print("3. Encontrar elemento")
        print("4. Mostrar fila")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            elemento = input("Informe o elemento a ser inserido: ")
            q.fila_inserir(elemento)
        elif escolha == '2':
            q.fila_remover()
        elif escolha == '3':
            elemento = input("Informe o elemento a ser encontrado: ")
            q.fila_encontrar(elemento)
        elif escolha == '4':
            q.fila_mostrar()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
