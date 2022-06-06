from gerenciador_recursos import GerenciadorRecursos
from abc import ABC, abstractmethod

class Recurso(ABC):
    @property
    def tipo(self):
        return self.__class__.__name__
    
    # Implemente aqui o resto da classe
    def __init__(self, nome):
        self.nome = nome
        self._num_tarefas = 0
        self.ocupado = False
    
    def reserva(self, tarefas):
        if self.ocupado is not True:
            self._num_tarefas += tarefas
            self.ocupado = True
    
    @abstractmethod
    def processa(self):
        if self._num_tarefas is not 0:
            self._num_tarefas -= 1
            if self._num_tarefas is 0:
                self.libera()
            return True
        else:
            self.libera()
            return False
    
    def libera(self):
        self.ocupado = False
        self._num_tarefas = 0

    def __repr__(self):
        return f'Recurso: {self.nome}, Tarefas: {self._num_tarefas}, Ocupado: {self.ocupado}'

class Impressora(Recurso):
    def __repr__(self):
        return super().__repr__() + f', Tipo: {self.tipo}'

    def processa(self):
        super().processa()
        if super().processa():
            print('Realizando impressao... impressao feita com sucesso')

class Cafeteira(Recurso):
    def __repr__(self):
        return super().__repr__() + f', Tipo: {self.tipo}'

    def processa(self):
        super().processa()
        if super().processa():        
            print('Fazendo café... café pronto')

def main():
    g = GerenciadorRecursos()

    r1 = Cafeteira('cafeteira1')
    r2 = Cafeteira('cafeteira2')
    r3 = Impressora('impressora1')
    r4 = Impressora('impressora2')
    g.adiciona(r1)
    g.adiciona(r2)
    g.adiciona(r3)
    g.adiciona(r4)
    print('>>> Estado Inicial:')
    g.imprime_recursos()
    print('')

    g.reserva('Cafeteira', 1)
    g.reserva('Impressora', 1)
    print('\n>>> Após reservar:')
    g.imprime_recursos()
    print('')

    g.processa_todos()
    print('\n>>> Após processar tarefas:')
    g.imprime_recursos()
    print('')

    g.reserva('Cafeteira', 5)
    g.reserva('Cafeteira', 1)
    g.libera('cafeteira1')
    print('\n>>> Após reservar e liberar:')
    g.imprime_recursos()
    print('')
    
if __name__ == "__main__":
    main()