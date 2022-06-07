class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'Pessoa{self.nome, self.idade}'

    def compara_idades(self, p2):
        '''Retorna verdadeiro se self for mais novo que p2.'''
        return self.idade <= p2.idade
    
    def cumprimenta(self, p):
        '''Cumprimenta um objeto p do tipo Pessoa'''
        print(f'Olá {p.nome}, tudo bem?')
    
    @staticmethod
    def media_idades(idades):
        media = 0
        for i in idades:
            media += i.idade
        media /= len(idades)
        return media

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula = 2022001):
        Pessoa.__init__(self, nome, idade)
        self.matricula = matricula

    def __repr__(self):
        return f'Aluno{self.nome, self.idade, self.matricula}'

class Professor(Pessoa):
    def __init__(self, nome, idade, departamento = 4):
        super().__init__(nome, idade)
        self.departamento = departamento

    def __repr__(self):
        return f'Professor{self.nome, self.idade, self.departamento}'
    
def main():
    p1 = Pessoa('Pedroa', 20)
    a1 = Aluno('Lucas', 18)
    prof1 = Professor('Maria', 48)

    l = [p1, a1, prof1]

    print('A média das idades é igual a {:.2f}'.format(Pessoa.media_idades(l)))
    
if __name__ == "__main__":
    main()

