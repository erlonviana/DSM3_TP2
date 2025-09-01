#2 Construa um programa que receba a variação do deslocamento de um objeto (em metros)
#e a variação do tempo percorrido (em segundos). Ao fim, o programa deve calcular
#a velocidade media em m/s do objeto vm=d/t

deslocamento = input("Informe a distancia percorrida em metros")
tempo = input("Informe o tempo decorrido em segundos")

vm = deslocamento/tempo

print("A velocidade media eh" + vm)