from meu_tk import *

class BuscadorDeVideos(tk.Tk):
    def __init__(self):
        super().__init__()
        self._configs_iniciais()

        # Atributos públicos
        self.botoes = dict()
        self.widgets = dict()
        self.frames = dict()
        self.tv = None

        self.draw()

    def _configs_iniciais(self):
        self.title('Buscador de Vídeos')
        self.minsize(720, 480)
        self.columnconfigure(0, weight=3)
        self.rowconfigure(1, weight=1)

    def draw(self):
        # Barra de pesquisa
        form = Frame(self, (0, 0), bd=10, relief=tk.SUNKEN, sticky='NSWE')
        l1 = Label(form, 'Buscar:', (0, 0))
        e1 = Entry(form, (0, 1), sticky='WE')
        b1 = Button(form, '🔍', (0, 2))
        self._config_form(form)

        # Dados
        datas = Frame(self, (1, 0), bd=10, relief=tk.SUNKEN, sticky='NSWE')
        nb = Notebook(datas, (0, 0), sticky='NSWE')
        tabela = Frame(nb, (0, 0), sticky='NSWE')
        grafico = Frame(nb, (0, 0), sticky='NSWE')
        nb.adicionar_frame(tabela, 'Resultados')
        nb.adicionar_frame(grafico, 'Gráficos')
        c, t, n = self._config_tv()
        self.tv = TreeView(tabela, c, t, n, (0, 0), sticky='NSWE')
        infos = Frame(tabela, (2, 0), sticky='NSWE')
        l2 = Label(infos, 'Mostrando:', position=(0, 0))
        b2 = Button(infos, 'Mostrar mais', position=(0, 1))
        l3 = Label(infos, 'Tamanho da lista:', position=(0, 2))
        self._config_datas(datas, tabela, infos)

        # Configurações
        frame_pad = Frame(self, (0, 1), bd=10, relief=tk.SUNKEN, sticky='NSWE')
        configs = Frame(frame_pad, (0, 0))
        l4 = Label(configs, 'Pesquisar por:', (0, 0), sticky='W')
        v = ['titulo', 'canal', 'categoria', 'periodo']
        cb = ComboBox(configs, values=v, position=(1, 0))
        cb.bind('<<ComboboxSelected>>', self.cb_opcao)
        cb_frame = Frame(configs, (2, 0), sticky='W')
        l5 = Label(cb_frame, 'Escolha o tipo de pesquisa...', (0, 0), sticky='W')

        Separator(configs, orient='horizontal', position=(3, 0), sticky='WE')

        l6 = Label(configs, 'Gráfico:', position=(4, 0), sticky='W')
        opcoes = Frame(configs, (5, 0), sticky='WE')
        t = ['mais assistidos', 'mais likes', 'mais comentários']
        v = ['assistidos', 'likes', 'comentários']
        rb = RadioButton(opcoes, t, v, (0, 0))
        b6 = Button(configs, 'Mostrar gráfico', (6, 0))
        reset = Frame(frame_pad, (1, 0), sticky='S')
        b3 = Button(reset, 'Resetar', (0, 0))
        self._config_configs(configs, frame_pad, reset)

        # Opções
        opcoes = Frame(self, (2, 0), bd=10, relief=tk.SUNKEN, sticky='NSWE')
        l7 = Label(opcoes, 'Arquivo: ', (0, 0), sticky='W')
        b5 = Button(opcoes, 'Importar dados', (0, 1))
        opcoes.grid(columnspan=2)
        opcoes.columnconfigure(0, weight=1)

        # Define atributos públicos
        widgets_opcoes = opcoes.winfo_children()
        for widget in widgets_opcoes:
            widget.grid(padx=5, pady=5)

        self.botoes['grafico'] = b6
        self.widgets['arquivo'] = l7
        self.botoes['importar'] = b5
        self.widgets['tam_lista'] = l3
        self.widgets['mostrando'] = l2
        self.botoes['pesquisar'] = b1
        self.widgets['barra_pesquisa'] = e1
        self.widgets['cb'] = cb
        self.frames['cb_frame'] = cb_frame
        self.widgets['tipo_pesquisa'] = l5
        self.botoes['resetar'] = b3
        self.widgets['rb'] = rb
        self.botoes['mais'] = b2

        widgets_font = [l1, e1] + [b5] + [l4, l6, cb]
        b1.font('', 13)
        self._configura_widgets(widgets_font)

    def _configura_widgets(self, l):
        for i in l:
            i.font('', 15)

    # Métodos auxiliares
    def _config_form(self, f):
        f.columnconfigure(1, weight=1)
        f.columnconfigure(0, pad=10)
        f.columnconfigure(2, pad=10)
        f.rowconfigure(0, pad=10)
        f.rowconfigure(2, pad=10)

    def _config_datas(self, datas, tabela, infos):
        infos.rowconfigure(0, pad=10)
        infos.columnconfigure(0, pad=10)

        datas.columnconfigure(0, weight=1)
        datas.rowconfigure(0, weight=1)
        tabela.columnconfigure(0, weight=1)
        tabela.rowconfigure(0, weight=1)
        infos.columnconfigure(0, weight=1)
        infos.rowconfigure(0, weight=1)

        infos.columnconfigure(0, weight=1)
        infos.columnconfigure(2, weight=1)

    def _config_tv(self):
        c = ['col0', 'col1', 'col2', 'col3', 'col4']
        t = ['Id', 'Titulo', 'Canal', 'Views', 'Likes']
        n = [100, 400, 200, 100, 100]
        return c, t, n

    def _config_configs(self, configs, frame_pad, reset):
        frame_pad.rowconfigure(1, weight=1)
        reset.rowconfigure(0, pad=10)
        configs.rowconfigure(6, pad=10)
        configs.rowconfigure(1, pad=10)
        configs.rowconfigure(3, pad=10)
        configs.rowconfigure(4, pad=10)
        frame_pad.rowconfigure(0, pad=10)
        frame_pad.columnconfigure(0, pad=10)
        frame_pad.grid(rowspan=2)

    def cb_opcao(self, event):
        cb_frame = self.frames['cb_frame']
        cb = self.widgets['cb']
        l5 = self.widgets['tipo_pesquisa']
        l5.texto = ''
        if cb.texto == '':
            l5.texto = 'Escolha o tipo de pesquisa...'
        elif cb.texto == 'titulo':
            l5.texto = 'Digite o título na barra de pesquisa.'
        elif cb.texto == 'canal':
            l5.texto = 'Digite o nome do canal na barra de pesquisa.'
        elif cb.texto == 'categoria':
            # Label(configs, 'Digite o nome do canal na barra de pesquisa.', (2, 0), sticky='W')
            e1 = Entry(cb_frame, (1, 0), sticky='W')

def main():
    v = BuscadorDeVideos()
    v.mainloop()

if __name__ == '__main__':
    main()