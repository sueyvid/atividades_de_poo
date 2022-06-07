class Calendario():

    ultimo_dia_mes = (31,28,31,30,31,30,31,31,30,31,30,31)

    @staticmethod
    def ehBissexto(ano):
        """ 
        O metodo retorna True se o parametro ano é ano bissexto, False caso contrario
        """
        # para ser ano bissexto:
        #     é ano % 4 == 0
        # nao é ano % 100 == 0
        # nao é ano % 400 == 0
        if ano % 4 == 0 and ano % 100 != 0 and ano % 400 != 0:
            return True
        elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
            return True
        else:
            return False


    def __init__(self, dia, mes, ano):
        self.__dias = 0
        self.__meses = 0
        self.__anos = 0
        self.set_data(dia, mes, ano)

    def set_data(self, dia, mes, ano):
        """
        dia, mes e ano devem ser numeros inteiros
        """
        self.__dias = dia
        self.__meses = mes
        self.__anos = ano

    def __str__(self):
        return "{0:02d}/{1:02d}/{2:4d}".format(self.__dias,
                                               self.__meses,
                                               self.__anos)
    
    def avanca_dia(self):
        """
        Avança um dia no calendário.
        """
        #verifique qual o ultimo dia do mes
        #verifique se mes de fevereiro é bissexto
        #se o dia é o ultimo do mes atual, dia tem valor 1
        #se o dia é o ultimo do ano, mes tem valor 1 e ano += 1
        #para todos os outros casos apenas dia é incrementado
        if Calendario.ehBissexto(self.__anos):
            fevereiro = 29
        else:
            fevereiro = 28
        
        if self.__dias < fevereiro and self.__meses == 2:
            self.__dias += 1
        elif self.__dias < Calendario.ultimo_dia_mes[self.__meses-1]:
            self.__dias += 1
        else:
            self.__meses += 1
            self.__dias = 1
        if self.__meses > 12:
            self.__anos += 1
            self.__meses = 1

def main():
    c = Calendario(31,12,2012)
    print(c, end=" ")
    c.avanca_dia()
    print("- Ao avancar um dia vamos para a data: ", c)
    print("2012 é ano Bissexo:")
    c = Calendario(28,2,2012)
    print(c, end=" ")
    c.avanca_dia()
    print("- Ao avancar um dia vamos para a data: ", c)
    c = Calendario(28,2,2013)
    print(c, end=" ")
    c.avanca_dia()
    print("- Ao avancar um dia vamos para a data: ", c)
    print("1900 não é ano Bissexo. O número é divisivel por 100 mas não por 400: ")
    c = Calendario(28,2,1900)
    print(c, end=" ")
    c.avanca_dia()
    print("- Ao avancar um dia vamos para a data: ", c)
    print("2000 foi um é ano Bissexo. O número é divisivel por 400: ")
    c = Calendario(28,2,2000)
    print(c, end=" ")
    c.avanca_dia()
    print("- Ao avancar um dia vamos para a data: ", c)

        
if __name__ == "__main__":
    main()