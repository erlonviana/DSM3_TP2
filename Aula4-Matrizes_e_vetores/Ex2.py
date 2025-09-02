# Crie uma matriz[4,4] de inteiros
# que leia 16 valores , conte e 
# escreva quantos valores maiores 
# que 10 a matriz possui.

import numpy as np
linhas = int(4)
colunas = int(4)

matriz = [16]
for i in range(linhas): 
    linha = [] #cria um novo vetor chamado linha
    matriz.append(linha)
    for j in range(colunas):
        numero = float(input(f"Digite o numero para a posição ({i}, {j}): "))
        linha.append(numero)

print(matriz)