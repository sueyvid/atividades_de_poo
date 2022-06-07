from math import sqrt, pi
from abc import ABC, abstractmethod

class Figura(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

class TrianguloEquilatero(Figura):
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura
    
    @property
    def area(self):
        return (self._base*self._altura)/2

    @property
    def perimetro(self):
        return self._base + (sqrt(self._base**2 + self._altura**2)*2)

    def __repr__(self):
        return f'(base: {self._base}, altura: {self._altura}, area: {self.area:.5f}, perimetro: {self.perimetro:.5f})'

class Quadrado(Figura):
    def __init__(self, lado):
        self._lado = lado
    
    @property
    def area(self):
        return self._lado**2

    @property
    def perimetro(self):
        return self._lado*4

    def __repr__(self):
        return f'(lado: {self._lado}, area: {self.area:.5f}, perimetro: {self.perimetro:.5f})'

class Circulo(Figura):
    def __init__(self, raio):
        self._raio = raio
    
    @property
    def area(self):
        return pi*self._raio**2

    @property
    def perimetro(self):
        return 2*pi*self._raio

    def __repr__(self):
        return f'(raio: {self._raio}, area: {self.area:.5f}, perimetro: {self.perimetro:.5f})'

def main():
    c = Circulo(2)
    q = Quadrado(3)
    tr = TrianguloEquilatero(2, 3)
    l = [c, q, tr]

    for carac in l:
        print(carac)
        print(carac.area)
        print(carac.perimetro)

if __name__ == '__main__':
    main()