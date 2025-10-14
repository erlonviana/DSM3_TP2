# Crie um vetor para digitar 
# nomes de Times de Futebol , 
# sem especificar o tamanho do 
# vetor e mostrar os nomes dos 
# times no final.

# import numpy as np
# tamanho = int(input("Informe o tamanho do vetor: "))

# vetor = []

# for i in range(tamanho):
#     elemento = (input(f"Digite o time {i + 1} do vetor: "))
#     vetor.append(elemento) #função append adiciona elemento dentro do vetor

# print("Vetor: ", vetor)

times = input("Digite os times separados por espaço")

#vetor = [tipo(x) for x in vetor.split]

vetor = [str(x) for x in times.split()]

print(vetor)