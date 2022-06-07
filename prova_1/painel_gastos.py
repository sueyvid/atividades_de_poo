class PainelGastos:
    def __init__(self):
        self._gastos = list()
    
    def adiciona_gasto(self, gasto):
        self._gastos.append(gasto)

    def remove_gasto(self, id):
        i = 0
        for e in self._gastos:
            if id == e.id:
                self._gastos.pop(i)
                print(f'gasto de id {e.id} removido com sucesso')
                break
            elif e == self._gastos[-1]:
                print(f'gasto com id {id} não encontrado')
            i += 1
    
    def atualiza_gasto(self, valor, categoria, id):
        i = 0
        for e in self._gastos:
            if e.id == id:
                self._gastos[i].valor = valor
                self._gastos[i].categoria = categoria
                print(f'gasto com id {e.id} atualizado com sucesso')
            i += 1

    def imprime_gastos(self):
        for e in self._gastos:
            print(e)

    def obtem_informacoes(self):
        total_valor = 0
        i = 0
        for e in self._gastos:
            total_valor += e.valor
            i += 1
        print(f'{i} gastos. Total: R${total_valor}.00')