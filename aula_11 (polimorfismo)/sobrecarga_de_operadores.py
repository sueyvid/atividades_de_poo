class Ponto2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'Ponto2D({self.x}, {self.y})'
    
    def __add__(self, p2 = None):
        if isinstance(p2, tuple):
            x = self.x + p2[0]
            y = self.y + p2[1]
            return x, y
        if isinstance(p2, Ponto2D):
            x = self.x + p2.x
            y = self.y + p2.y
            return Ponto2D(x, y)
    
    def __mul__(self, p2 = None):
        if isinstance(p2, int):
            p2 = float(p2)
        if isinstance(p2, float):
            x = self.x * p2
            y = self.y * p2
            return Ponto2D(x, y)
        if isinstance(p2, Ponto2D):
            x = self.x * p2.x
            y = self.y * p2.y
            return x + y
    
    def __eq__(self, p2 = None):
        if isinstance(p2, tuple) and self.x == p2[0] and self.y == p2[1]:
            return True
        else:
            return False
        if isinstance(p2, Ponto2D) and self.x == p2.x and self.y == p2.y:
            return True
        else:
            return False
        
    def __getitem__(self, i):
        if i == 0:
            return self.x
        if i == 1:
            return self.y
    
    def __setitem__(self, i, v):
        if i == 0:
            self.x = v
        if i == 1:
            self.y = v

def main():
    p1 = Ponto2D(2.0, -2.0)
    p2 = Ponto2D(-2.0, 2.0)
    print(p1 + p2) # retorna Ponto2D
    print(p1 + (5.0, 5.0)) # retorna tupla

    p3 = p1 * 4 # multiplica por escalar, retorna Ponto2D
    print(p3)

    print(p1 * p2) # produto interno/escalar, retorna nr. real

    print(p3 == (8.0, -8.0))
    print(p3 == p1)
    
    p1[0] = 7.0
    p1[1] = 6.0
    print(f'x: {p1[0]}, y: {p1[1]}')

if __name__ == '__main__':
    main()