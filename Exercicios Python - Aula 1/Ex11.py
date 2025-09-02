#Ler a descrição do produto (nome), a qtd comprada e o preço. Exibir o total e a descrição

Nome = str(input("Insira o nome do produto: "))
Preco = float(input("Insira o preço unitario do produto: "))
Qtd = int(input("Insira a quantidade comprada: "))

Total = Qtd * Preco

print(f"Produto: {Nome} Valor total: R${Total:.2f}")