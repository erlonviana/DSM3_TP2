# Leia 6 nomes de Capitais do Brasil e guarde 
# numa matriz[2,3] , e mostre todas as 
# Capitais.

import numpy as np
linhas = int(2)
colunas = int(3)

matriz = [6]
for i in range(linhas): 
    linha = [] #cria um novo vetor chamado linha
    matriz.append(linha)
    for j in range(colunas):
        numero = (input(f"Digite a capital para a posição ({i}, {j}): "))
        linha.append(numero)

print(matriz)