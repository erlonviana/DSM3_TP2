# Crie uma matriz[4,4] de inteiros
# que leia 16 valores , conte e 
# escreva quantos valores maiores 
# que 10 a matriz possui.

# import numpy as np
# linhas = int(4)
# colunas = int(4)

# matriz = [16]
# for i in range(linhas): 
#     linha = [] #cria um novo vetor chamado linha
#     matriz.append(linha)
#     for j in range(colunas):
#         numero = float(input(f"Digite o numero para a posição ({i}, {j}): "))
#         linha.append(numero)

# print(matriz)

matriz = []
maioresquedez = 0 # Inicialização da variável de contagem

#Matriz 4x4
for i in range(4):
    linha = []
    matriz.append(linha)
    for j in range(4):
        numero = int(input(f"Digite o inteiro inteiro na posição {i+1}, {j+1}: "))
        linha.append(numero)
        if numero > 10:
            maioresquedez += 1

for i in range(4):
    print(matriz[i])
    
print(f"Existem {maioresquedez} números maiores que 10")