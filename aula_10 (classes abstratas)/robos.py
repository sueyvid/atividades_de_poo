from abc import ABC, abstractmethod

class Posicao:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Robo(ABC):
    def __init__(self, posicao):
        self.posicao = posicao
    
    @abstractmethod
    def move(self):
        pass

    @property
    def informaPosicao(self):
        return self.posicao.x, self.posicao.y

class RoboOmnidirecional(Robo):
    def move(self, posFinal):
        self.posicao = posFinal

class RoboComRodas(Robo):
    def move(self, dx, dy):
        self.posicao.x += dx
        self.posicao.y += dy

class RoboQuadrupede(Robo):
    def move(self, dx, dy):
        self.posicao.x += dx
        self.posicao.y += dy

def main():
    pos1 = Posicao(2, 3)
    pos2 = Posicao(4, 5)
    pos3 = Posicao(2, 2)

    Robo1 = RoboOmnidirecional(pos1)
    Robo2 = RoboComRodas(pos2)
    Robo3 = RoboQuadrupede(pos3)

    l = [Robo1, Robo2, Robo3]

    for i, robo in enumerate(l):
        print(f'robo {i+1}: {robo.informaPosicao}')
    
    novaPos = Posicao(3, 5)
    dx, dy = 2, 3

    Robo1.move(novaPos)
    Robo2.move(dx, dy)
    Robo3.move(dx, dy)

    for i, robo in enumerate(l):
        print(f'robo {i+1}: {robo.informaPosicao}')

if __name__ == '__main__':
    main()