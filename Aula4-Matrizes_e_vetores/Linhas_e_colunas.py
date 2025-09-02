linhas = int(input("Digite o numero de linhas da matriz: "))
colunas = int(input("Digite o numero de colunas da matriz: "))

matriz_numeros = [] #vetor chamado matriz_numeros
for i in range(linhas): 
    linha = [] #cria um novo vetor chamado linha
    matriz_numeros.append(linha)
    for j in range(colunas):
        numero = float(input(f"Digite o numero para a posição ({i}, {j}): "))
        linha.append(numero)