import random

class Produto:
    def __init__(self, preco):
        self._codigo = random.randint(100, 999)
        self._preco = preco
        self._desconto = False
        
    def preco_com_desconto(self, porcentagem):
        preco = self._preco-(self._preco*porcentagem)
        return f'{preco:.2f}'
    
    def ativa_desconto(self):
        self._desconto = True
        
    def __str__(self):
        r = f'\nCod: {self._codigo}: R${self._preco:.2f}'
        r += f'\nPreço com desconto: R$'
        return r
    
class Livro(Produto):
    def __init__(self, titulo, autor, preco):
        Produto.__init__(self, preco)
        self._titulo = titulo
        self._autor = autor
        
    def preco_com_desconto(self):
        if self._desconto == True:
            r = str(super().preco_com_desconto(0.3))
        else:
            r = f'{self._preco:.2f}'
        return r
        
    def __str__(self):
        r = f'Livro: {self._titulo} - {self._autor}'
        r += super().__str__()
        r += str(self.preco_com_desconto())
        r += '\n'
        return r
        
class Jogo(Produto):
    def __init__(self, nome, plataforma, preco):
        Produto.__init__(self, preco)
        self._nome = nome
        self._plataforma = plataforma
    
    def preco_com_desconto(self):
        if self._desconto == True:
            if self._plataforma == 'PS4':
                p = 0.18
            elif self._plataforma == 'Xbox One':
                p = 0.2
            else:
                p = 0.1
            r = str(super().preco_com_desconto(p))
        else:
            r = f'{self._preco:.2f}'
        return r
    
    def __str__(self):
        r = f'Jogo: {self._nome} - {self._plataforma}'
        r += super().__str__()
        r += str(self.preco_com_desconto())
        r += '\n'
        return r

def main():
    l1 = Livro('O homem duplicado', 'Jose Saramago', 30.00)
    l2 = Livro('O idiota', 'Fiodor Dostoievski', 35.00)
    l2.ativa_desconto()
    l3 = Livro('Revolução dos bichos', 'George Orwell', 35.00)
    j1 = Jogo('Street Fighter V', 'PS4', 200.00)
    j2 = Jogo('Call of Duty: Black Ops Cold War', 'PS4', 250.00)
    j2.ativa_desconto()
    j3 = Jogo('Call of Duty: Black Ops Cold War', 'Xbox One', 250.00)
    j3.ativa_desconto()
    j4 = Jogo('Forza Horizon 4', 'Xbox One', 200.00)
    j5 = Jogo('Zelda: Breath of the Wild', 'Switch', 300.00)
    j5.ativa_desconto()

    l = [l1, l2, l3, j1, j2, j3, j4, j5]
    for prod in l:
        print(prod)
    
if __name__ == '__main__':
    main()