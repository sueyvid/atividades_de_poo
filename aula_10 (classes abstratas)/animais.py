from abc import ABC, abstractmethod

class Animal(ABC):
    def nasce(self):
        print('Nasceu')
    
    def morre(self):
        print('Morreu')
        
    @abstractmethod
    def emite_som(self):
        pass
    
class Mamifero(Animal):
    def amamenta(self):
        print('Amamentou')
        
class Ave(Animal):
    def voa(self):
        print('Voou')
        
class Gato(Mamifero):
    def emite_som(self):
        return ('miau')

class Cachorro(Mamifero):
    def emite_som(self):
        return ('au au')

class Ornitorrinco(Mamifero):
    def emite_som(self):
        return ('ha ha')

class Pinguim(Ave):
    def emite_som(self):
        return ('in in')

class Aguia(Ave):
    def emite_som(self):
        return ('aaahh')

def main():
    a1 = Pinguim()
    a2 = Ornitorrinco()
    a3 = Gato()
    a4 = Cachorro()
    a5 = Aguia()
    l = [a1, a2, a3, a4, a5]
    for som in l:
        print(som.emite_som())

if __name__ == '__main__':
    main()