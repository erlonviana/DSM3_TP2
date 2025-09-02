# Crie um vetor, leia 10 posições de numeros inteiros, armazene os valores e mostre

import numpy as np

tamanho = int(10)

vetor = np.empty(tamanho, dtype=int)

for i in range(tamanho):
    elemento = int(input(f"Digite o elemento {i+1} do vetor: "))
    vetor[i] = elemento

print("Vetor: ", vetor)