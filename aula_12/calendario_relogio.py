from relogio import Relogio
from calendario import Calendario

class CalendarioRelogio(Calendario, Relogio):
    def __init__(self, dia, mes, ano, hora, minuto, segundo):
        Calendario.__init__(self, dia, mes, ano)
        Relogio.__init__(self, hora, minuto, segundo)
    
    def ehBissexto(self, ano):
        super().ehBissexto(ano)
        
    def marca_segundo(self):
        Relogio.marca_segundo(self)
        if self._horas == 0:
            Calendario.avanca_dia(self)
        
    def __str__(self):
        r = Calendario.__str__(self)
        r += ', '
        r += Relogio.__str__(self)
        r += ' '
        return r

def main():
    cr = CalendarioRelogio(31, 12, 2013, 23, 59, 59)
    print("Passou um segundo de", cr, end=" ")
    cr.marca_segundo()
    print("para", cr)

    cr = CalendarioRelogio(7, 2, 2013, 13, 55, 40)
    print("Passou um segundo de", cr, end=" ")
    cr.marca_segundo()
    print("para", cr)

if __name__ == "__main__":
    main()