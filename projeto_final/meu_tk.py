import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
from abc import ABC, abstractmethod


class Posicionamento(ABC):
    @abstractmethod
    def __str__(self):
        return 'Método abstrato'

    def set_pack(self):
        '''
        Configura o posicionamento do widget
        utilizando pack
        '''
        self.pack()

    def set_grid(self, row, column, sticky=None):
        '''
        Configura o posicionamento do widget
        utilizando grid, recebe os parâmetros
        row e column
        '''
        self.grid(row=row, column=column, sticky=sticky)

    def _posiciona(self, position=None, row=None, column=None, sticky=None):
        '''
        Define se o posicionamento do widget
        será feito utilizando pack ou grid,
        dependendo dos valores dos parâmetros
        position, row e column
        '''
        if position is None and row is None and column is None:
            self.set_pack()
        elif isinstance(position, tuple):
            self.set_grid(row=position[0], column=position[1], sticky=sticky)
        elif isinstance(position, int) and row is not None and column is None:
            self.set_grid(row=position, column=row, sticky=sticky)
        elif row is not None and column is not None:
            self.set_grid(row=row, column=column, sticky=sticky)

class TextoDinamico:
    def cria_var(self, texto_inicial=''):
        '''
        Cria um StringVar para ser usado
        por um widget
        '''
        self._texto = tk.StringVar()
        self._texto.set(texto_inicial)
        return self._texto

    @property
    def texto(self):
        return self._texto.get()
    
    @texto.setter
    def texto(self, s):
        self._texto.set(s)

class Janela(tk.Tk):
    def __init__(self, nome=None):
        super().__init__()
        self.title(nome)

class Frame(tk.Frame, Posicionamento):
    def __init__(self, root, position=None, row=None, column=None, bd=None, relief=None, sticky=None):
        super().__init__(root, bd=bd, relief=relief)
        super()._posiciona(position, row, column, sticky)

class Notebook(ttk.Notebook, Posicionamento):
    def __init__(self, root, position=None, row=None, column=None, sticky=None):
        super().__init__(root)
        super()._posiciona(position, row, column, sticky)

    def adicionar_frame(self, frame, text):
        self.add(frame, text=text)

class ConfiguraWidget(TextoDinamico, Posicionamento):
    def posiciona(self, position=None, row=None, column=None, sticky=None):
        super()._posiciona(position, row, column, sticky)

    def cria_texto_var(self, texto):
        t = super().cria_var(texto)
        return t

    def font(self, fonte='', tamanho=None):
        self['font'] = (fonte, tamanho)

class Label(tk.Label, ConfiguraWidget):
    def __init__(self, root, texto, position=None, row=None, column=None, sticky=None):
        t = self.cria_texto_var(texto)
        super().__init__(root, textvariable=t)
        self.posiciona(position, row, column, sticky)

class Entry(tk.Entry, ConfiguraWidget):
    def __init__(self, root, position=None, row=None, column=None, texto='', sticky=None):
        t = self.cria_texto_var(texto)
        super().__init__(root, textvariable=t)
        self.posiciona(position, row, column, sticky)

class Button(tk.Button, ConfiguraWidget):
    def __init__(self, root, texto, position=None, row=None, column=None, sticky=None):
        t = self.cria_texto_var(texto)
        super().__init__(root, textvariable=t)
        self.posiciona(position, row, column, sticky)

    def command(self, f):
        self['command'] = f

class ExploradorDeArquivo(ConfiguraWidget):
    tipos_arq = (
        ('Arquivo csv', '*.csv'),
        ('Arquivos de texto', '*.txt'),
        ('Todos os arquivos', '*.*')
    )
    def __init__(self, tipos, texto=''):
        t = self.cria_texto_var(texto)
        
        nome_arq = askopenfilename(title='Abrir arquivo',\
                                filetypes=tipos)
        if nome_arq:
            t.set(nome_arq)

    def __str__(self):
        return 'Explorador de Arquivos'

class ComboBox(ttk.Combobox, ConfiguraWidget):
    def __init__(self, root, values, state='readonly', position=None, row=None, column=None, sticky=None):
        t = self.cria_texto_var('')
        super().__init__(root, textvariable=t, values=values, state=state)
        self.posiciona(position, row, column, sticky)
        self.bind('<<ComboboxSelected>>', self.mostra_selecao)

    def mostra_selecao(self, event):
        s = self._texto.get()
        print(s)

class Separator(ttk.Separator, Posicionamento):
    def __init__(self, root, orient, position=None, row=None, column=None, sticky=None):
        super().__init__(root, orient=orient)
        self._posiciona(position, row, column, sticky)

class RadioButton(tk.Radiobutton, ConfiguraWidget):
    def __init__(self, root, texts, values, position=None, row=None, column=None, sticky=None):
        t = self.cria_texto_var('')
        for i in range(len(values)):
            super().__init__(root, text=texts[i], value=values[i], variable=t)
            self.set_grid(i, 0, sticky='W')


class TreeView(ttk.Treeview, Posicionamento):
    def __init__(self, tela, colunas, titulos, tamanhos, position=None, row=None, column=None, sticky=None):
        super().__init__(tela, columns=colunas, show='headings')

        for i in range(len(colunas)):
            self.heading(colunas[i], text=titulos[i])
            self.column(colunas[i], width=tamanhos[i]-50, minwidth=tamanhos[i])

        self.sb(tela)
        super()._posiciona(position, row, column, sticky)

    def sb(self, tela):
        sb_y = ttk.Scrollbar(tela, orient=tk.VERTICAL, command=self.yview)
        self.configure(yscroll=sb_y.set)

        sb_x = ttk.Scrollbar(tela, orient=tk.HORIZONTAL, command=self.xview)
        self.configure(xscroll=sb_x.set)

        sb_y.grid(row=0, column=1, sticky='NS')
        sb_x.grid(row=1, column=0, sticky='WE')

    def insere(self, parent, pos, values):
        self.insert(parent, pos, values=values)

    def remove(self):
        tup = self.selection()
        index = list()
        for i, v in enumerate(tup):
            pos = tup[i]
            index.append(self.index(pos))
        for i, v in enumerate(tup):
            self.delete(v)
        return index

    def limpa(self):
        for i in self.get_children():
            self.delete(i)

def main():
    janela = Janela('TreeView')

    f = Frame(janela, 1, 0)
    # Button(f, 'texto inicial')
    # b = f.Button('texto inicial')
    # b.texto = 'outro nome'
    # l.texto = 'outro'
    # l = LabelDinamico(f, 'texto inicial', 0, 0)
    # l.text = '123'

    f2 = Frame(janela, 0, 0)
    col = ['col0', 'col1', 'col2']
    tit = ['Titulo', 'Ano', 'Nota']
    tam = [200, 40, 40]

    treeview = TreeView(f2, col, tit, tam, (0,0))
    for i in range(20):
        treeview.insere('', 0, values=['nada', 'nada', 'nada'])

    b = Button(f, 'remover', (0,0))
    b.command(treeview.remove)

    janela.mainloop()

if __name__ == '__main__':
    main()