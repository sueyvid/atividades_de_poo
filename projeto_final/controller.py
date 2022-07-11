from interface import *
from modelo import *

class Controller:
    def __init__(self):
        self.view = None
        self.model = None
        self.fila = None
        self.qtd_mostrando = 0

    def inicia(self, view):
        self.view = view
        self._configura()
        
    def _configura(self):
        # self.view.buttons[1].command(self.insere_dados)
        # cb.bind('<<ComboboxSelected>>', self.mostra_selecao)

        bt_resetar = self.view.botoes['resetar']
        bt_resetar.command(self.resetar)

        bt_pesquisar = self.view.botoes['pesquisar']
        bt_pesquisar.command(self.insere_dados)

        bt_importar_dados = self.view.botoes['importar']
        bt_importar_dados.command(self.importar_dados)

        bt_mostrar_grafico = self.view.botoes['grafico']
        bt_mostrar_grafico.command(self.mostrar_grafico)

        bt_mostrar_mais = self.view.botoes['mais']
        bt_mostrar_mais.command(self.adiciona_na_lista)

    def resetar(self):
        cb = self.view.widgets['cb']
        cb.texto = ''
        pesquisa = self.view.widgets['barra_pesquisa']
        pesquisa.texto = ''
        self.insere_dados()

    def mostrar_grafico(self):
        rb = self.view.widgets['rb']
        if rb.texto == '':
            print('erro')
        elif rb.texto == 'assistidos':
            self.model.mostra_mais_assistidos()
        elif rb.texto == 'likes':
            self.model.mostra_mais_likes()
        elif rb.texto == 'comentários':
            self.model.mostra_mais_comentarios()
        
    def importar_dados(self):
        tipo_de_arq = ExploradorDeArquivo.tipos_arq
        e = ExploradorDeArquivo(tipo_de_arq)

        nome_do_arq = e.texto
        if nome_do_arq == '':
            print('erro')
        exibe_nome_arquivo = self.view.widgets['arquivo']
        exibe_nome_arquivo.texto = nome_do_arq
        m = BancoDadosYT(nome_do_arq)
        self.model = m

        self.insere_dados()

    def insere_dados(self):
        cb = self.view.widgets['cb']
        self.qtd_mostrando = 0
        self.view.tv.limpa()

        pesquisa = self.view.widgets['barra_pesquisa'].get()
        if cb.texto == '':
            res = self.model.todos()
        elif pesquisa == '':
            print('erro')
        elif cb.texto == 'titulo':
            res = self.model.busca_por_titulo(pesquisa)
        elif cb.texto == 'canal':
            res = self.model.busca_por_canal(pesquisa)
        elif cb.texto == 'categoria':
            res = self.model.busca_por_canal(pesquisa)
            print(self.model.categorias)

        self.fila = res.copy()
        self.adiciona_na_lista()

        exibe_tam_lista = self.view.widgets['tam_lista']
        exibe_tam_lista.texto = f'Tamanho da lista: {len(res)}'

    def adiciona_na_lista(self):
        res = self.fila
        self.qtd_mostrando
        for i in range(len(res)):
            if i < 5:
                id = res[i].id_video
                titulo = res[i].titulo
                canal = res[i].canal
                views = res[i].cont_views
                likes = res[i].likes
                self.view.tv.insere('', tk.END, values=[id, titulo, canal, views, likes])
                self.qtd_mostrando += 1
        for i in range(len(res)):
            if i < 5:
                res.pop(0)
        n = self.qtd_mostrando
        exibe_mostrando = self.view.widgets['mostrando']
        exibe_mostrando.texto = f'Mostrando: {n}'
    
def main():
    v = BuscadorDeVideos()
    c = Controller()
    c.inicia(v)
    v.mainloop()

if __name__ == '__main__':
    main()