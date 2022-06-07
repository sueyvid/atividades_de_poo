from abc import ABC, abstractmethod

class Animal(ABC):
    '''Classe abstrata'''
    def __init__(self, peso = None):
        self.nasce()
        self.peso = peso

    @abstractmethod
    def nasce(self):
        pass

    def morre(self):
        print('Animal morreu')

    @abstractmethod
    def emite_som(self):
        pass
    
    @staticmethod
    def media_pesos(L):
        media = 0
        for animal in L:
            media += animal.peso
        media /= len(L)
        return media

class Mamifero(Animal):
    '''Abstrata: não implementa o método emite_som'''
    
    def amamenta(self):
        print('Mamífero amamentou')
        
    def nasce(self):
        print('Mamífero nasceu do ventre')

class Ave(Animal):
    '''Abstrata: não implementa o método emite_som'''
    
    def voa(self):
        print('Ave voou')
        
    def nasce(self):
        print('Ave nasceu do ovo')
    
    def pode_voar(self):
        return True
    
    @staticmethod
    def podem_voar(L):
        l = list()
        for animal in L:
            if animal.pode_voar():
                l.append(animal)
        return l

class Gato(Mamifero):
    
    def emite_som(self):
        print('Miau')

class Cachorro(Mamifero):
    
    def emite_som(self):
        print('Au')

class Ornitorrinco(Mamifero):
    
    def emite_som(self):
        print('Prprpr')
        
    def nasce(self):
        print('Ornitorrinco nasceu do ovo')

class Pinguim(Ave):
    
    def emite_som(self):
        print('Quack')
        
    def voa(self):
        print('Pinguim não voa')
        
    def pode_voar(self):
        return False

class Aguia(Ave):
    
    def emite_som(self):
        print('In')

def main():
    print('#Nascimento dos animais: ')
    p1 = Pinguim(20)
    a1 = Aguia(16)

    L = [p1, a1]

    l = Ave.podem_voar(L)

    print('\n#Animais que voam: ')
    for animal in l:
        animal.emite_som()

    print('\n#Média dos pesos: ')
    print('A média dos pesos dos animais é igual a {}'.format(Animal.media_pesos(L)))
        
if __name__ == "__main__":
    main()