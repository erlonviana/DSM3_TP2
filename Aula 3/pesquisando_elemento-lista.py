localizar = "banana"
fruits = ["maça", "banana", "laranja"]
for fruit in fruits:
    if fruit == localizar:
        print(f"Encontrado: {localizar}")
        break
else:
    print(f"{localizar} não encontrado")