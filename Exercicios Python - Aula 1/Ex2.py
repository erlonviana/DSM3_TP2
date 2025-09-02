#Um programa que receba a variação de deslocamento e o tempo decorrido e calcule a velocidade média

Deslocamento = float(input("Informe a distancia percorrida em metros"))
Tempo = int(input("Informe o tempo decorrido em segundos"))

Vm = Deslocamento / Tempo

print(f"A velocidade media é {Vm:.2f} m/s")