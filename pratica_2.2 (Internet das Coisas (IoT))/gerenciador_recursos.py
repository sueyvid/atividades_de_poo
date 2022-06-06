class GerenciadorRecursos:
    def __init__(self):
        self._recursos = []

    def _busca_recurso(self, nome):
        '''
        Retorna um recurso que tenha como
        nome o parâmetro informado.
        '''

        for r in self._recursos:
            if r.nome == nome:
                return r
        else:
            return None

    def _busca_recurso_livre(self, tipo):
        '''
        Retorna o primeiro recurso não ocupado
        que seja do tipo do parâmetro informado.
        '''

        for r in self._recursos:
            if not r.ocupado and r.tipo == tipo:
                return r
        else:
            return None

    def adiciona(self, rec):
        '''
        Adiciona recurso ao gerenciador.
        '''

        self._recursos.append(rec)

    def imprime_recursos(self):
        '''
        Imprime todos os recursos.
        '''

        for r in self._recursos:
            print(r)

    def reserva(self, tipo, n):
        '''
        Reserva um recurso de tipo
        informado para uso para
        realizar n tarefas
        '''

        r = self._busca_recurso_livre(tipo)
        if r:
            r.reserva(n)
            print(f'>Recurso {r.nome} reservado')
        else:
            print(f'>Não há recurso do tipo {tipo} livre')

    def processa_todos(self):
        '''
        Processa todos os recursos
        '''
        for r in self._recursos:
            r.processa()

    def libera(self, nome_rec):
        '''
        Libera o recurso de nome
        informado
        '''
        
        r = self._busca_recurso(nome_rec)
        if r:
            r.libera()