class Livro:
    ISBN = list()
    def __init__(self, t = '', a = 0, c = 0):
        self._titulo = t
        self._ano = a
        self._codigo = c
    
    def __str__(self):
        return f'titulo: {self._titulo}, ano: {self._ano}, ISBN: {self._codigo}'
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def ano(self):
        return self._ano
    
    @property
    def codigo(self):
        return self._codigo
    
    @titulo.setter
    def titulo(self, t):
        if t == '':
            raise TituloVazio('O título do livro não pode ser uma string vazia.')
        else:
            self._titulo = t
    
    @ano.setter
    def ano(self, a):
        if a <= 1400 or a >= 2100:
            raise AnoInvalido('O ano de um livro deve estar entre 1400 e 2100.')
        else:
            self._ano = a
    
    @codigo.setter
    def codigo(self, c):
        if c <= 99999:
            raise CodigoInvalido('O ISBN de um livro deve conter pelo menos 6 caracteres.')
        else:
            for codigo in Livro.ISBN:
                if codigo == c:
                    raise ConflitoDeCodigo('Já existe um livro com o mesmo código.')
            for codigo in Livro.ISBN:
                if codigo == self._codigo:
                    Livro.ISBN.remove(self._codigo)
            self._codigo = c
            Livro.ISBN.append(c)

class ErroBiblioteca(Exception):
    pass

class TituloVazio(ErroBiblioteca):
    pass

class AnoInvalido(ErroBiblioteca):
    pass

class CodigoInvalido(ErroBiblioteca):
    pass

class LivroEsperado(ErroBiblioteca):
    pass

class ConflitoDeCodigo(ErroBiblioteca):
    pass

class LivroArmazenado(ErroBiblioteca):
    pass

class Biblioteca:
    def __init__(self, nome):
        self._nome = nome
        self._lista = list()
    
    def __str__(self):
        s = f'Biblioteca: {self._nome}'
        for livro in self._lista:
            s += '\n > '
            s += str(livro)
        return s
    
    def cadastrar(self, livro):
        if isinstance(livro, Livro):
            for l in self._lista:
                if l._codigo == livro._codigo:
                    raise LivroArmazenado('O livro contém o mesmo ISBN de um livro já armazenado.')
            self._lista.append(livro)
        else:
            raise LivroEsperado('O parâmetro deve ser do tipo livro.')

def main():
    bib = Biblioteca('BCZM')
    print(bib)
    
    l1 = Livro()
    l2 = Livro()
    bib.cadastrar(l1)
    book = not Livro()
    for i in range(6):
        try:
            if i == 0: l1.titulo = ''
            if i == 1: l1.ano = 1200
            if i == 2: l1.codigo = 123
            if i == 3: bib.cadastrar(book)
            if i == 4: l2.codigo = l1.codigo
            if i == 5: bib.cadastrar(l1)
        except TituloVazio as err:
            titulo = ''
            while(titulo == ''):
                print('TituloVazio:', err)
                titulo = input('Digite o nome do livro: ')
            l1.titulo = titulo
        except AnoInvalido as err:
            ano = 1200
            while(ano <= 1400 or ano >= 2100):
                print('AnoInvalido:', err)
                ano = int(input('Digite um ano válido: '))
            l1.ano = ano
        except CodigoInvalido as err:
            codigo = 123
            while(codigo <= 99999):
                print('CodigoInvalido:', err)
                codigo = int(input('Digite um codigo válido: '))
            l1.codigo = codigo
        except LivroEsperado as err:
            print('LivroEsperado:', err)
        except ConflitoDeCodigo as err:
            print('ConflitoDeCodigo:', err)
        except LivroArmazenado as err:
            print('LivroArmazenado:', err)
    
    print('-'*20)
    print(bib)

    print('Livros: ')
    print(l1)

    print('ISBNs:')
    for i in (Livro.ISBN):
        print(f'> {i}')

if __name__ == '__main__':
    main()