from meu_tk import *

class BuscadorDeVideos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Buscador de Vídeos')
        self.buttons = list()
        self.tv = None
        self._config_tela()
        self.draw()

    def _config_tela(self):
        self.minsize(380, 400)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

    def _config_form(self, f):
        f.columnconfigure(1, weight=1)
        f.columnconfigure(0, pad=10)
        f.columnconfigure(2, pad=10)

    def _config_datas(self, f):
        f.columnconfigure(0, weight=1)
        f.rowconfigure(0, weight=1)

    def _config_tv(self):
        c = ['col0', 'col1', 'col2', 'col3', 'col4']
        t = ['Id', 'Titulo', 'Canal', 'Views', 'Likes']
        n = [100, 400, 200, 100, 100]
        return c, t, n

    def draw(self):
        form = Frame(self, (0, 0), bd=10, relief=tk.SUNKEN, sticky='NSWE')
        l1 = Label(form, 'Buscar:', (0, 0))
        e1 = Entry(form, (0, 1), sticky='WE')
        b1 = Button(form, '🔍', (0, 2))
        self._config_form(form)

        datas = Frame(self, (1, 0), bd=10, relief=tk.SUNKEN, sticky='NSWE')
        c, t, n = self._config_tv()
        self.tv = TreeView(datas, c, t, n, (0, 0), sticky='NSWE')
        self._config_datas(datas)

        opcoes = Frame(self, (2, 0), bd=10, relief=tk.SUNKEN, sticky='NSWE')
        opcoes.grid(columnspan=2)
        l2 = Label(opcoes, 'Arquivo: ', (0, 0), sticky='W')
        b2 = Button(opcoes, 'Inserir dados', (0, 1))
        b3 = Button(opcoes, 'Importar dados', (0, 2))
        opcoes.columnconfigure(0, weight=1)

        b = [b1, b2, b3, l2]
        self.buttons.extend(b)

        todos_widgets = list()
        widgets_form = form.winfo_children()
        widgets_opcoes = opcoes.winfo_children()
        
        for widget in widgets_opcoes:
            widget.grid(padx=5, pady=5)
        
        todos_widgets.extend(widgets_form)
        todos_widgets.extend(widgets_opcoes)
        self._configura_widgets(todos_widgets)

    def _configura_widgets(self, l):
        for i in l:
            i.font('', 15)

def main():
    v = BuscadorDeVideos()
    v.mainloop()

if __name__ == '__main__':
    main()