#Ler o total de votos brancos, nulos e validos. Faça a soma do numero total de eleitores
#Caclular e escrever o percentual que cada um representa em relação ao total de eleitores.

Validos = int(input("Insira o total de votos validos: "))
Nulos = int(input("Insira o total de votos nulos: "))
Brancos = int(input("Insira o total de votos brancos: "))

Total = Validos + Nulos + Brancos

Validos = (Validos/Total)*100
Nulos = (Nulos/Total)*100
Brancos = (Brancos/Total)*100

print(f"""O total de votos é {Total:.2f}, sendo que {Validos:.2f} % são Válidos, {Nulos:.2f} % são nulos e 
      {Brancos:.2f} % são Brancos""")