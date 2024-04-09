class Aluno:
    def __init__(self, nome, sexo, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.matricula = matricula

if __name__ == '__main__':
    aluno1 = Aluno("hendeson", "m", "16", "123456")
    print(aluno1.nome)
    print(aluno1.idade)
    print(aluno1.matricula)
    print(aluno1.sexo)