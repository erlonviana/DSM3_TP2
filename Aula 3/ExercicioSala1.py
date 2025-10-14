#Faça um programa que verifique se uma letra digitada é consoante ou vogal

letra = input("Digite a letra: ")

#forma mais difícil
# match letra:
#     case 'a':
#         print("Voce digitou uma vogal")
#     case 'e':
#         print("Voce digitou uma vogal")
#     case 'i':
#         print("Voce digitou uma vogal")
#     case 'o':
#         print("Voce digitou uma vogal")
#     case 'u':
#         print("Voce digitou uma vogal")
#     case _:
#         print("Voce digitou uma consoante")

match letra.lower():
    case 'a'| 'e' | 'i' | 'o' | 'u':
        print("Voce digitou uma vogal")
    case _:
        print("Voce digitou uma consoante")


#Executando python sem extensão
# ctrl j - abrir o terminal

# cd aula 03 (abrindo a pasta certa)

# python + nome do arquivo (precisa estar dentro da pasta)