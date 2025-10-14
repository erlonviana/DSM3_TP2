# Crie um vetor para ler 5 
# cores mostre as cores 
# armazenadas no vetor

import numpy as np

vetor = [5]

for i in range(5):
    elemento = (input(f"Digite a cor {i + 1} do vetor: "))
    vetor.append(elemento) #função append adiciona elemento dentro do vetor

print("Vetor: ", vetor)