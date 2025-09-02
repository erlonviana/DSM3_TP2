# vetor = [10, 20, 30, 40]
# print(vetor)

tamanho = int(input("Digite o tamanho do vetor: "))

vetor = []

for i in range(tamanho):
    elemento = int(input(f"Digite o elemento {i + 1} do vetor: "))
    vetor.append(elemento) #função append adiciona elemento dentro do vetor

print("Vetor: ", vetor)

#Sobercarga de método é quando um método aceita diferentes chamadas

#instalar biblioteca numpy para números: pip install numpy

