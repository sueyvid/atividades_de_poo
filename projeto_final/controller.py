from interface import *
from modelo import *

class Controller:
    def __init__(self):
        self.view = None
        self.model = None

    def inicia(self, view, model):
        self.view = view
        self.model = model
        self._configura()
        
    def _configura(self):
        self.view.buttons[1].command(self.insere_dados)
        
    def insere_dados(self):
        res = self.model.busca_por_periodo('2020-11-01', '2020-11-30')
        id = res[0].id_video
        print(id)
        # self.view.tv.insere('', 0, values=[id, ])
        # for v in res:
        #     print(v)
    
def main():
    v = BuscadorDeVideos()
    m = BancoDadosYT('BR_youtube_trending_data_p1.csv')
    c = Controller()
    c.inicia(v, m)
    v.mainloop()
    

if __name__ == '__main__':
    main()