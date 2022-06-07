import math

class Complexo:
    # implemente o código da classe
    def __init__(self, r, im):
        self.r = r
        self.im = im
    
    def reset(self):
        self.r = 0.0
        self.im = 0.0
    
    def __str__(self):
        return f'{self.r} + {self.im}i'
    
    def __add__(self, Z2):
        r = self.r + Z2.r
        im = self.im + Z2.im
        Z3 = Complexo(r, im)
        return Z3
    
    def modulo(self):
        return (self.r**2 + self.im**2) ** (1/2)

def main():
    '''Função principal do programa.'''
    
    c1 = Complexo(2, 3)
    c2 = Complexo(10, 7)
    print(c1)
    print(c2)

    c3 = c1 + c2
    print(c3)
    print(c3.modulo())

    c3.reset()
    print(c3)
    
if __name__ == '__main__':
    main()