from random import randint

class Gasto:
    def __init__(self):
        self._valor = 0
        self._categoria = ''
        self._id = randint(0, 10000)
    
    @property
    def valor(self):
        return self._valor

    @property
    def categoria(self):
        return self._categoria
    
    @property
    def id(self):
        return self._id

    @valor.setter
    def valor(self, outro):
        self._valor = outro
    
    @categoria.setter
    def categoria(self, outro):
        self._categoria = outro
    
    def __str__(self):
        return f'{self._id} - {self._categoria}: R${self._valor}.00'