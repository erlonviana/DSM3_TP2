numeros = []

for i in range(1,5):
    numero = float(input(f"Digite o {i}º numero: "))
    numeros.append(numero)

print("Numeros digitados: ")
for numero in numeros:
    print(numero)