from obra import Obra

class Museu:
    pass
    def __init__(self, nome, obras):
        self._nome = nome
        self._obras = list()
        for i in obras:
            self._obras.append(Obra(i[0], i[1], i[2]))

    def imprime_obras(self):
        t = f'Obras do museu "{self._nome}":'
        for e in self._obras:
            t += '\n    '
            t += f'{e}'
        print(t)

    def remove_obra(self, titulo):
        for obra in self._obras:
            if titulo in obra._obra:
                self._obras.remove(obra)