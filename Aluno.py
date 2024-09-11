Class Aluno: 
    def__init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    def_str__(self):
        return "Aluno{"+"nome=" + self.nome + "idade" + self.idade + '}'
    
    def __eq__(self, object):