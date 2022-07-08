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
        self.view.buttons[2].command(self.importar_dados)
        
    def importar_dados(self):
        nome_do_arq = 'BR_youtube_trending_data_p1.csv'
        m = BancoDadosYT(nome_do_arq)
        self.model = m
        self.view.buttons[3].texto = nome_do_arq

        self.view.tv.limpa()
        # tipo_de_arq = ExploradorDeArquivo.tipos_arq
        # e = ExploradorDeArquivo(tipo_de_arq)
        # self.view.buttons[3].texto = e.texto

    def insere_dados(self):
        res = self.model.busca_por_periodo('2020-11-01', '2020-11-30')
        self.view.tv.limpa()
        for i in range(len(res)):
            id = res[i].id_video
            titulo = res[i].titulo
            canal = res[i].canal
            views = res[i].cont_views
            likes = res[i].likes
            self.view.tv.insere('', 0, values=[id, titulo, canal, views, likes])
    
def main():
    v = BuscadorDeVideos()
    c = Controller()
    c.inicia(v)
    v.mainloop()

if __name__ == '__main__':
    main()