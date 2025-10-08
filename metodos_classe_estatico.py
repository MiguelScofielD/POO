class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)

    @staticmethod
    def maior_idade(idade):
        return idade >= 18


P = Pessoa.criar_de_data_nascimento(1996, 9, 23, "Antonio Santana")
print(P.nome, P.idade)

print(P.maior_idade(P.idade))
