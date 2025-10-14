#Um algoritmo para calcular Tensão, Resistência e corrente:

opcao = int(input("\n 1 - Tensão \n 2 - Resistencia \n 3 - Corrente \n Escolha a opcao:"))

match opcao:
    case 1:
        print("Escolheu a opcao tensão (U) em Volts")
        resistencia = float(input("Informe a resistencia em Ohm: "))
        corrente = float(input("Informe a corrente em Ampere: "))
        tensão = resistencia*corrente
        print(f"A tensão é de {tensão} Volt(s)")
    case 2:
        print("Escolheu a opcao Resistencia (R) em Ohm")
        tensão = float(input("Digite a tensão em Volts: "))
        corrente = float(input("Informe a corrente em Ampere: "))
        resistencia= tensão/corrente
        print(f"A resistencia é de {resistencia} Ohms")

    case 3:
        print("Escolheu a opção corrente (i) em Ampere")
        tensão = float(input("Digite a tensão em Volts: "))
        resistencia = float(input("Informe a resistencia em Ohm: "))
        corrente = tensão/resistencia
        print(f"A corrente é de {corrente} Amperes")
    case _:
        print("Opcao invalida")
