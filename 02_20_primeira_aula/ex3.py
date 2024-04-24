"""
Questão 3

Faça um programa para ler 10 números DIFERENTES a serem armazenados
em um vetor. Os dados deverão ser armazenados no vetor na ordem que
forem sendo lidos, sendo que caso o usuário digite um número que já foi
digitado anteriormente, o programa deverá pedir para ele digitar outro número.
Note que cada valor digitado pelo usuário deve ser pesquisado no vetor,
verificando se ele existe entre os números que já foram fornecidos. Exibir na
tela o vetor final que foi digitado.
"""

# Inicializa um vetor vazio para armazenar os números
numeros = []

# Loop para ler 10 números diferentes
for i in range(10):
    while True:
        # Solicita ao usuário que digite um número
        numero = int(input("Digite um número: "))
        # Verifica se o número já foi digitado antes
        if numero in numeros:
            print("Esse número já foi digitado. Por favor, digite outro número.")
        else:
            # Adiciona o número ao vetor
            numeros.append(numero)
            break

# Exibe o vetor final
print("Vetor final:", numeros)


"""
Neste código, utilizamos um loop for para solicitar ao usuário que digite 10 números diferentes. Utilizamos um loop while dentro do loop for para garantir que cada número digitado seja único. Se o número já estiver presente no vetor, o programa pedirá ao usuário que digite outro número. Quando o usuário inserir um número válido, ele será adicionado ao vetor. Após o término do loop, o programa exibe o vetor final.
"""