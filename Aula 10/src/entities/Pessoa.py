class Pessoa:
    def __init__(self, nome, idade, ativo):
        self.nome = nome
        self.idade = idade
        self.ativo = ativo

    def ativar(self):
        self.ativo = True
        print("A pessoa foi ativada com sucesso")

    def desativar(self):
        self.ativo = False
        print("A pessoa foi desativada")

    def mostrarDados(self):
        print(f"O nome da pessoa é {self.nome} \n ela tem {self.idade} anos \n Situação da pessoa (Ativo: Sim = True, Não = False) {self.ativo}")