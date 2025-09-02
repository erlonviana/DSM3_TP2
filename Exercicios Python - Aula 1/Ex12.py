#Calcule quantos azulejos são necessarios para azulejar uma parede. Necessario base e altura
#da parede e do azulejo. Calcular também as áreas de cada um.

BaseParede = float(input("Insira a base da parede em metros: "))
AlturaParede = float(input("Insira a altura da parede em metros: "))
BaseAzulejo = float(input("Insira a base do azulejo cm: "))
AlturaAzulejo = float(input("Insira a altura do azulejo: "))

Parede = BaseParede * AlturaParede 
Azulejo = BaseAzulejo * AlturaAzulejo

Qtd = int((Parede*100)/Azulejo)

print(f"""A area da parede é {Parede} m2 e a area do azulejo é {Azulejo} cm2.
Serão necessarios {Qtd} azulejos""")