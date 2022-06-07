class Obra:
    pass
    def __init__(self, obra, autor, ano):
        self._obra = obra
        self._autor = autor
        self._ano = ano
    
    def __str__(self):
        return f'{self._obra}, {self._autor} ({self._ano})'