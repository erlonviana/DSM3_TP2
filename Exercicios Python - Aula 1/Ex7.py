#Faça um algoritmo que leia o nome e a idade de uma pessoa e exiba o nome e quantos dias
#essa pessoa já viveu

Nome = str(input("Insira seu nome"))
Idade = int(input("Insira sua idade"))

Idade = Idade * 365

print(f"Seu nome é {Nome} e sua idade em dias é {Idade}")