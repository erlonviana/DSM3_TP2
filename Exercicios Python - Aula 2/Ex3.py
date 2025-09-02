# Escreva um programa que solicite ao usuário a estatura de 3 pessoas. Ao fim, o
# programa deve mostrar as estaturas em ordem decrescente.

Pessoa1 = float(input("Informe a estatura da pessoa 1: "))
Pessoa2 = float(input("Informe a estatura da pessoa 2: "))
Pessoa3 = float(input("Informe a estatura da pessoa 3: "))

if Pessoa1 > Pessoa2 and Pessoa2 > Pessoa3:
    print(f"{Pessoa3}, {Pessoa2}, {Pessoa1}");

elif Pessoa2 > Pessoa1 and Pessoa1 > Pessoa3:
    print(f"{Pessoa3} "," {Pessoa1}, {Pessoa2}");

elif Pessoa3 > Pessoa2 and Pessoa2 > Pessoa1:
    print(f"{Pessoa1}, {Pessoa2}, {Pessoa3}");

elif Pessoa2 > Pessoa3 and Pessoa3 > Pessoa1:
    print(f"{Pessoa1}, {Pessoa3}, {Pessoa2}");

elif Pessoa3 > Pessoa1 and Pessoa1 > Pessoa2:
    print(f"{Pessoa2}, {Pessoa1}, {Pessoa3}")

elif Pessoa1 > Pessoa3 and Pessoa3 > Pessoa2:
    print(f"{Pessoa2}, {Pessoa3}, {Pessoa1}")