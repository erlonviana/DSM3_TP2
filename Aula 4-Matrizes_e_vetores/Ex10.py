# Crie uma matriz, que leia 5 produtos e sua 
# quantidade, e coloque em matriz[5,2], na 
# primeira coluna armazena o nome produto e 
# na segunda coluna a quantidade.

# import numpy as np
# linhas = int(5)
# colunas = int(2)

# matriz = []
# for i in range(linhas): 
#     linha = [] #cria um novo vetor chamado linha
#     matriz.append(linha)
#     for j in range(colunas):
#         numero = int(input(f"Digite o numero para a posição ({i}, {j}): "))
#         linha.append(numero)

# print(matriz)

linhas = 5
colunas = 2

matriz = []

for i in range(linhas):
    linha = []
    # Lendo o nome do produto (string)
    nome_produto = input(f"Digite o nome do produto {i + 1}: ")
    linha.append(nome_produto)
    
    # Lendo a quantidade (inteiro)
    quantidade = int(input(f"Digite a quantidade de {nome_produto}: "))
    linha.append(quantidade)
    
    matriz.append(linha)

# Mostrando a matriz completa
print("\nMatriz de produtos e quantidades:")
for linha in matriz:
    print(linha)