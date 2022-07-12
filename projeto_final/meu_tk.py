import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
from abc import ABC, abstractmethod


class Posicionamento(ABC):
    @abstractmethod
    def __str__(self):
        pass

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

class ConfiguraWidget(TextoDinamico, Posicionamento):
    def posiciona(self, position=None, row=None, column=None, sticky=None):
        '''
        Posiciona o widget
        '''
        super()._posiciona(position, row, column, sticky)

    def cria_texto_var(self, texto):
        '''
        Cria uma variável StringVar do tk
        '''
        t = super().cria_var(texto)
        return t

    def font(self, fonte='', tamanho=None):
        '''
        Formata a fonte do widget
        '''
        self['font'] = (fonte, tamanho)

class Janela(tk.Tk):
    def __init__(self, nome=None):
        '''
        Cria uma janela tk
        '''
        super().__init__()
        self.title(nome)

class Frame(tk.Frame, Posicionamento):
    def __init__(self, root, position=None, row=None, column=None, bd=None, relief=None, sticky=None):
        '''
        Cria um frame tk
        '''
        super().__init__(root, bd=bd, relief=relief)
        super()._posiciona(position, row, column, sticky)

class Notebook(ttk.Notebook, Posicionamento):
    def __init__(self, root, position=None, row=None, column=None, sticky=None):
        '''
        Cria um notebook tk
        '''
        super().__init__(root)
        super()._posiciona(position, row, column, sticky)

    def adicionar_frame(self, frame, text):
        '''
        Adiciona um frame ao notebook
        '''
        self.add(frame, text=text)

class Label(tk.Label, ConfiguraWidget):
    def __init__(self, root, texto, position=None, row=None, column=None, sticky=None):
        '''
        Cria um Label tk com uma
        StringVar associada
        '''
        t = self.cria_texto_var(texto)
        super().__init__(root, textvariable=t)
        self.posiciona(position, row, column, sticky)

class Entry(tk.Entry, ConfiguraWidget):
    def __init__(self, root, position=None, row=None, column=None, texto='', sticky=None):
        '''
        Cria um Entry tk com uma
        StringVar associada
        '''
        t = self.cria_texto_var(texto)
        super().__init__(root, textvariable=t)
        self.posiciona(position, row, column, sticky)

class Button(tk.Button, ConfiguraWidget):
    def __init__(self, root, texto, position=None, row=None, column=None, sticky=None):
        '''
        Cria um Button tk com uma
        StringVar associada
        '''
        t = self.cria_texto_var(texto)
        super().__init__(root, textvariable=t)
        self.posiciona(position, row, column, sticky)

    def command(self, f):
        '''
        Define qual função será chamada
        ao clicar no botão, passando-a
        como parâmetro
        '''
        self['command'] = f

class ExploradorDeArquivo(ConfiguraWidget):
    tipos_arq = (
        ('Arquivo csv', '*.csv'),
        ('Arquivos de texto', '*.txt'),
        ('Todos os arquivos', '*.*')
    )
    def __init__(self, tipos, texto=''):
        '''
        Abre o buscador do windows e
        armazena o nome do arquivo em
        uma StringVar
        '''
        t = self.cria_texto_var(texto)
        
        nome_arq = askopenfilename(title='Abrir arquivo',\
                                filetypes=tipos)
        if nome_arq:
            t.set(nome_arq)

    def __str__(self):
        return 'Explorador de Arquivos'

class Separator(ttk.Separator, Posicionamento):
    def __init__(self, root, orient, position=None, row=None, column=None, sticky=None):
        '''
        Cria um Separator tk
        '''
        super().__init__(root, orient=orient)
        self._posiciona(position, row, column, sticky)

class ComboBox(ttk.Combobox, ConfiguraWidget):
    def __init__(self, root, values, state='readonly', position=None, row=None, column=None, sticky=None):
        '''
        Cria um Combobox tk com uma
        Stringvar associada
        '''
        t = self.cria_texto_var('')
        super().__init__(root, textvariable=t, values=values, state=state)
        self.posiciona(position, row, column, sticky)

class RadioButton(TextoDinamico):
    def __init__(self, root, texts, values, position=None, row=None, column=None, sticky=None):
        '''
        Cria um ou mais RadioButton
        em um frame com uma StringVar
        associada
        '''
        t = self.cria_var('')
        self.rb = list()
        for i in range(len(values)):
            r = ttk.Radiobutton(root, text=texts[i], value=values[i], variable=t)
            r.grid(row=i, column=0, sticky='W')
            self.rb.append(r)
    
    def retorna_rb(self):
        '''
        Retorna a lista de RadioButton
        que foram criados
        '''
        return self.rb

class TreeView(ttk.Treeview, Posicionamento):
    def __init__(self, tela, colunas, titulos, tamanhos, position=None, row=None, column=None, sticky=None):
        '''
        Cria um Treeview tk com as
        chaves e os titulos sendo passados
        como listas nos parâmetros
        '''
        super().__init__(tela, columns=colunas, show='headings')

        for i in range(len(colunas)):
            self.heading(colunas[i], text=titulos[i])
            self.column(colunas[i], width=tamanhos[i]-50, minwidth=tamanhos[i])

        self._sb(tela)
        super()._posiciona(position, row, column, sticky)

    def _sb(self, tela):
        sb_y = ttk.Scrollbar(tela, orient=tk.VERTICAL, command=self.yview)
        self.configure(yscroll=sb_y.set)

        sb_x = ttk.Scrollbar(tela, orient=tk.HORIZONTAL, command=self.xview)
        self.configure(xscroll=sb_x.set)

        sb_y.grid(row=0, column=1, sticky='NS')
        sb_x.grid(row=1, column=0, sticky='WE')

    def insere(self, parent, pos, values):
        '''
        Insere linha na Treeview
        recebendo posição e valor
        '''
        self.insert(parent, pos, values=values)

    def remove(self):
        '''
        Remove linha que tiver sido
        selecionada na Treeview
        '''
        tup = self.selection()
        index = list()
        for i, v in enumerate(tup):
            pos = tup[i]
            index.append(self.index(pos))
        for i, v in enumerate(tup):
            self.delete(v)
        return index

    def limpa(self):
        '''
        Remove todas as linhas de dados
        da Treeview
        '''
        for i in self.get_children():
            self.delete(i)