from meu_tk import *

class BuscadorDeVideos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Buscador de Vídeos')
        self.buttons = list()
        self.tv = None
        self.draw()

    def draw(self):
        form = Frame(self, (0, 0), bd=10, relief=tk.SUNKEN)
        l1 = Label(form, 'Buscar:', (0, 0))
        e1 = Entry(form, (0, 1))
        b1 = Button(form, '🔍', (0, 2))

        datas = Frame(self, (1, 0), bd=10, relief=tk.SUNKEN)
        c = ['col0', 'col1', 'col2', 'col3', 'col4']
        t = ['Id', 'Titulo', 'Canal', 'Views', 'Likes']
        n = [100, 100, 100, 100, 100]
        self.tv = TreeView(datas, c, t, n, (0, 0))
        b2 = Button(datas, 'Inserir dados', (1, 0))

        b = [b1, b2]
        self.buttons.extend(b)
        l = [l1, e1, b1, b2]
        self._configura(l)

    def _configura(self, l):
        for i in l:
            i.font('', 15)

def main():
    v = BuscadorDeVideos()
    v.mainloop()

if __name__ == '__main__':
    main()