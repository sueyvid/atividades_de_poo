from gasto import Gasto
from painel_gastos import PainelGastos

def main():
    g1 = Gasto()
    g1.valor = 50
    g1.categoria = 'Transporte'
    
    g2 = Gasto()
    g2.valor = 300
    g2.categoria = 'Saúde'

    g3 = Gasto()
    g3.valor = 400
    g3.categoria = 'Saude'

    g4 = Gasto()
    g4.valor = 100
    g4.categoria = 'Contas Mensais'

    g5 = Gasto()
    g5.valor = 200
    g5.categoria = 'Contas Mensais'

    g6 = Gasto()
    g6.valor = 200
    g6.categoria = 'Mercado'

    g7 = Gasto()
    g7.valor = 300
    g7.categoria = 'Mercado'

    g8 = Gasto()
    g8.valor = 100
    g8.categoria = 'Lazer'
    
    p = PainelGastos()
    p.adiciona_gasto(g1)
    p.adiciona_gasto(g2)
    p.adiciona_gasto(g3)
    p.adiciona_gasto(g4)
    p.adiciona_gasto(g5)
    p.adiciona_gasto(g6)
    p.adiciona_gasto(g7)
    p.adiciona_gasto(g8)

    p.imprime_gastos()
    p.obtem_informacoes()
    p.remove_gasto(100001)
    p.remove_gasto(g6.id)

    p.atualiza_gasto(700, 'Mercado', g7.id)

    p.imprime_gastos()
    p.obtem_informacoes()

if __name__ == '__main__':
    main()