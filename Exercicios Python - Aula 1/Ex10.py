#Calcular e exibir o volume de um cilindro

Raio = int(input("Insira o raio do cilindro em cm: "))
Altura = int(input("Insira a altura do cilindro em cm: "))

Volume = 3.14 * (Raio**2) * Altura

print(f"O volume deste cilindro é {Volume:.2f} ml ou cm3")