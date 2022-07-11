from interface import *
from modelo import *

class Controller:
    def __init__(self):
        self.view = None
        self.model = None

    def inicia(self, view):
        self.view = view
        self._configura()
        
    def _configura(self):
        self.view.buttons[1].command(self.insere_dados)
        # cb.bind('<<ComboboxSelected>>', self.mostra_selecao)

        bt_pesquisar = self.view.botoes['pesquisar']
        bt_pesquisar.command(self.insere_dados)

        bt_importar_dados = self.view.botoes['importar']
        bt_importar_dados.command(self.importar_dados)

        bt_mostrar_grafico = self.view.botoes['grafico']
        bt_mostrar_grafico.command(self.mostrar_grafico)

    # def pesquisar(self):


    def mostrar_grafico(self):
        self.model.mostra_mais_assistidos()
        
    def importar_dados(self):
        tipo_de_arq = ExploradorDeArquivo.tipos_arq
        e = ExploradorDeArquivo(tipo_de_arq)

        nome_do_arq = e.texto
        exibe_nome_arquivo = self.view.widgets['arquivo']
        exibe_nome_arquivo.texto = nome_do_arq
        m = BancoDadosYT(nome_do_arq)
        self.model = m

        self.insere_dados()

    def insere_dados(self):
        cb = self.view.widgets['cb']
        self.view.tv.limpa()

        pesquisa = self.view.widgets['barra_pesquisa'].get()
        if cb.texto == '':
            res = self.model.todos()
        if cb.texto == 'titulo':
            res = self.model.busca_por_titulo(pesquisa)
        if cb.texto == 'canal':
            res = self.model.busca_por_canal(pesquisa)
        if cb.texto == 'categoria':
            res = self.model.busca_por_canal(pesquisa)
            print(self.model.categorias)

        n = 0
        # res = self.model.busca_por_periodo('2020-11-01', '2020-11-30')
        for i in range(len(res)):
            if i < 10:
                id = res[i].id_video
                titulo = res[i].titulo
                canal = res[i].canal
                views = res[i].cont_views
                likes = res[i].likes
                self.view.tv.insere('', 0, values=[id, titulo, canal, views, likes])
                n += 1

        exibe_tam_lista = self.view.widgets['tam_lista']
        exibe_tam_lista.texto = f'Tamanho da lista: {len(res)}'
        exibe_mostrando = self.view.widgets['mostrando']
        exibe_mostrando.texto = f'Mostrando: {n}'
    
def main():
    v = BuscadorDeVideos()
    c = Controller()
    c.inicia(v)
    v.mainloop()

if __name__ == '__main__':
    main()