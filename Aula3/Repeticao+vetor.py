names = ["Jimmy", "Rose", "Max", "Nina", "Phillip"]

for name in names:
    if len(name) != 4: #pular nomes que não tenham 4 letras
        continue #continue faz o laço voltar no "for"

    print(f"Hello, {name}") #nomes com 4 letras são exibidos

    if name == "Nina": #nome Nina causa a quebra do loop
        break

print("Done!")