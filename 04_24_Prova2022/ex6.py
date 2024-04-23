"""
(2,0 pontos) Considere a seguinte estrutura:

 0  1  2  3 4  5  6  7  8  9
-25 4 -8 16 77 15 5 -10 19 31

Apresente quais seriam os passos para a execução da ordenação da estrutura
considerando o algoritmo Selection sort:

Percorra a matriz para encontrar o valor mais baixo.
Mova o valor mais baixo para a frente da parte não classificada da matriz.
Percorra a matriz novamente quantas vezes houver valores na matriz.

-25
Percorre a estrutura e compara
Mantem o -25 na 1a posição, pois não há elemento menor na estrutura

4
Percorre a estrutura e compara
Troca o 4 que está na posição 1, pelo -10 que está na posição 7

 0   1   2 3  4  5  6 7 8  9
-25 -10 -8 16 77 15 5 4 19 31

Continua a execução até a lista estar completamente ordenada.

FIM
"""