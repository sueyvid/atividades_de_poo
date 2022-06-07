class Relogio():

    def __init__(self, horas, minutos, segundos):
        self._horas = 0
        self.__minutos = 0
        self.__segundos = 0
        self.set_hora(horas, minutos, segundos)

    def set_hora(self, horas, minutos, segundos):
        """
        Atributo horas deve ser um valor inteiro entre 0 e 23
        Atributo minutos deve ser um valor inteiro entre 0 e 59
        Atributo segundos deve ser um valor inteiro entre 0 e 59
        """        
        self._horas = horas
        self.__minutos = minutos
        self.__segundos = segundos
            

    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self._horas,
                                                self.__minutos,
                                                self.__segundos)

    def marca_segundo(self):
        """
        Avança um segundo no relógio.
        """
        self.__segundos += 1
        if self.__segundos > 59:
            self.__minutos += 1
            self.__segundos = 0
        if self.__minutos > 59:
            self._horas += 1
            self.__minutos = 0
        if self._horas > 23:
            self._horas = 0

def main():
    r = Relogio(23,59,59)
    print(r)
    r.marca_segundo()
    print(r)
    
if __name__ == "__main__":
    main()