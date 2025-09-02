#Construa um programa que receba o peso de duas pessoas e diga qual a pessoa mais
#pesada e verifica se as pessoas têm o mesmo peso.

Pessoa1 = float(input("Insira o peso da pessoa 1: "))
Pessoa2 = float(input("Insira o peso da pessoa 2: "))

if Pessoa1 == Pessoa2:
    print("Pessoa 1 tem o peso igual a Pessoa 2")

elif Pessoa2 > Pessoa1:
    print("Pessoa 2 é a mais pesada")

elif Pessoa1 > Pessoa2:
    print("Pessoa 2 é a mais pesada")
