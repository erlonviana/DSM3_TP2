#Criar um algoritmo para o indice de poluição#

poluicao = int(input("Informe o índice de poluição: "))

match poluicao:
    case 0 | 1 | 2:
        print("Indice considerado aceitável")
    case 3 | 4 | 5:
        print("Indice de poluição alto, Suspender atividades Grupo 1")
    case 6 | 7:
        print("Indice de poluição alto, Suspender atividades Grupo 1")
    case _:
        print("Indice de poluição alto, Suspender atividades de todos os grupos")
