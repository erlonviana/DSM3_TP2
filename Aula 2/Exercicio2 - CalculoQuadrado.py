numero = int(input('Informe o numero desejado: '))

resultado = numero%2

if resultado == 0:
    quadrado = numero**2
    print("O numero é par e seu quadrado é", quadrado)
elif resultado > 0:
    cubo = numero**3
    print(f"O numero {numero} é impar e o seu cubo é {cubo}") #outra forma