"""
Elabore as funções de inserção, retirada e consulta para uma fila circular utilizando de arrays que contém 5 nodos.

Ajustar o código-fonte para gerar o falso overflow, mantendo as demais funcionalidades em perfeito funcionamento conforme o que foi discutido em aula (comportamento esperado para a fila circular).

O desafio irá gerar 1 ponto(extra) na nota da avaliação I da disciplina de estrutura de dados, caso entregue tudo corretamente.

Período:
Inicia em 26/03/2024 às 00h00 e finaliza em 09/04/2024 às 23h59
"""

import numpy as np

# Declarando o array de 5 posições e preencher com zeros
array = np.zeros(5)

# Função para inserir um elemento no array
def inserir(elemento):
    f = 0
    r = 0
    tam = 5
    for i in range(5):
        if f == tam:
            array[i] = elemento
            i = r = r + 1    
    print(array)
    
inserir(1)