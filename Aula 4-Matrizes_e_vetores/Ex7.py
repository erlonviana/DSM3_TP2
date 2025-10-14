# Crie uma matriz[5,2] leia 
# 10 posições de números 
# inteiros ,armazene os 
# valores e mostre.

import numpy as np
linhas = int(5)
colunas = int(2)

matriz = []
for i in range(linhas): 
    linha = [] #cria um novo vetor chamado linha
    matriz.append(linha)
    for j in range(colunas):
        numero = int(input(f"Digite o numero para a posição ({i}, {j}): "))
        linha.append(numero)

print(matriz)