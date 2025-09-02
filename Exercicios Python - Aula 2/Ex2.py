#Construa um programa que receba um número inteiro positivo informado pelo
# usuário. Caso ele seja par, o programa deve
# calcular o seu quadrado. Mas, se ele for ímpar,
# deve ser calculado o seu cubo. Ao fim, o
# programa deve mostrar o valor calculado e
# dizer se o número é impar ou par.

Numero = int(input("Insira um número inteiro positivo: "))

if Numero < 0:
    print("Este não é um número positivo!")

elif Numero % 2 == 0:
    Quadrado = Numero**2
    print(f"O numero {Numero} é par e seu quadrado é {Quadrado}")

else:
    Cubo = Numero**3
    print(f"O Numero {Numero} é impar e seu cubo é {Cubo} ")
