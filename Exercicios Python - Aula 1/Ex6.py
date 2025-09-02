#Escrever um algoritmo que leia o salario de um funcionario, o percentual de ajuste, calcular
#e escrever o valor do salario

Salario = int(input("Insira o valor do salario atual: "))
Ajuste = int(input("Insira o valor percentual do ajuste: "))

Salario = Salario + (Salario*(Ajuste/100))

print(f"O valor do salario atualizado é {Salario:.2f}")