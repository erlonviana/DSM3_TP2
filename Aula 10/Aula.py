class Pessoa: #nome de classe começa em maiusculo
    def init (self, nome, idade, ativo): #self é o "this" no Java
        self.nome = nome #todo atributo precisa ter o self como argumento
        self.idade = idade
        self._ativo = ativo

    def ativar (self):
        self. ativo = True
        print("A pessoa foi desativada com sucesso")


