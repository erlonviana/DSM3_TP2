from entities.Pessoa import Pessoa

#mostrando que este arquivo main é executável
if __name__ == "__main__":
    #criando objeto
    pessoa = Pessoa("Maylon", 30, True)

    pessoa.mostrarDados()