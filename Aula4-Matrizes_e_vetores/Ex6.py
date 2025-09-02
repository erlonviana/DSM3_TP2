# Crie um vetor que leia 
# valores inteiros , e mostre os 
# valores armazenados , e 
# mostre quais são pares

import numpy as np
tamanho = int(input("Informe o tamanho do vetor: "))

# Criando um array NumPy
vetor = np.zeros(tamanho, dtype=int) #vetor é uma lista do Python, e a operação vetor % 2 não funciona com listas nativas — isso só funciona com arrays do NumPy.

for i in range(tamanho):
    vetor[i] = int(input(f"Digite o valor {i + 1} do vetor: "))

print("Vetor completo: ", vetor)
pares = vetor[vetor % 2 == 0]
print("Valores pares: ", pares)