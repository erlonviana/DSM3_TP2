print('## Programa de emprestimos ##. \n Responda (0-Não e 1-Sim)')

negativado = int(input("Possui nome negativo? (0-Não e 1-Sim)"))
if negativado == 1:
    print("NÃO PODE REALIZAR EMPRÉTIMO!!!")
else:
    carteiraAssinada = int(input("Possui carteira assinada? (0-Não e 1-Sim)"))

    if carteiraAssinada == 0:
        print("NÃO PODE REALIZAR EMPRÉTIMO!!!")
    else:
        possuiCasaPropria = int(input("Possui casa propria? (0-Não e 1-Sim) "))

        if possuiCasaPropria == 0:
            print("NÃO PODE REALIZAR EMPRÉTIMO!!!")
        else:
            print("Conceder emprestimo :D")