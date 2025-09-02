# Crie uma matriz[4,4] de inteiros
# que leia 16 valores , conte e 
# escreva quantos valores maiores 
# que 10 a matriz possui.

import numpy as np
linhas = int(4)
colunas = int(4)

# matriz = []
# for i in range(linhas): 
#     linha = [] #cria um novo vetor chamado linha
#     matriz.append(linha)
#     for j in range(colunas):
#         numero = int(input(f"Digite o numero para a posição ({i}, {j}): "))
#         linha.append(numero)

# maior_que_dez = matriz [matriz > 10]
# print(maior_que_dez)

# Criando uma matriz NumPy vazia
matriz = np.zeros((linhas, colunas), dtype=int)

# Preenchendo a matriz
for i in range(linhas):
    for j in range(colunas):
        matriz[i, j] = int(input(f"Digite o numero para a posição ({i}, {j}): "))

# Filtrando valores maiores que 10
maiores_que_dez = matriz[matriz > 10]

print("Valores maiores que 10:", maiores_que_dez)
print("Quantidade de valores maiores que 10:", len(maiores_que_dez))