"""
Construa um programa que solicite ao usuário dois números
positivos. Em seguida, o programa deve apresentar o seguinte
menu.
1 Média ponderada, com pesos 2 e 3, respectivamente
2. Quadrado da soma dos 2 números
3. Cubo do menor número Escolha uma opção
"""

Numero1 = int(input("Insira o primeiro número inteiro positivo: "))
Numero2 = int(input("Insira o segundo número inteiro positivo: "))

if Numero1 <= 0 or Numero2 <= 0:
    print("Os numeros devem ser positivos!")

else:
    print("\n 1. Média ponderada (pesos 2 e 3) \n 2. Quadrado da soma dos 2 números \n 3. Cubo do menor número")

opcao = int(input("Escolha a opção:"))

if opcao == 1:
    media = (Numero1*2 + Numero2*3) / 5
    print(f"A media ponderada com pesos 2 e 3 é", media)

elif opcao == 2:
    quadrado = (Numero1 + Numero2) ** 2
    print(f"O quadrado da soma dos 2 numeros é", quadrado)

elif opcao == 3:
    menor = min(Numero1, Numero2)
    print(f"O cubo do menor numero é", menor **3)

else:
    print("Opção invalida")


