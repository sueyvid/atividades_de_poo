import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showerror, showinfo
from operator import itemgetter

########## Classes Modelo ##########
class Filme:
    def __init__(self, tit, ano, nota):
        self.titulo = tit
        self.ano = ano
        self.nota = nota

    def __str__(self):
        return f'{self.titulo} ({self.ano}) - {self.nota}'

class ListaFilmesModel:
    def __init__(self):
        self._filmes = []

    def insere_filme(self, f):
        self._filmes.append(f)

    def atualiza_filme(self, pos, novo_filme):
        self._filmes[pos] = novo_filme

    def remove_filme(self, pos):
        self._filmes.pop(pos)

    def converte_para_lista(self):
        '''
        Gera lista de strings para ser
        usada pela listbox.
        '''
        res = []
        for f in self._filmes:
            res.append(str(f))
        return res

    def converte_para_lista_tuplas(self):
        res = []
        for f in self._filmes:
            res.append((str(f.titulo), int(f.ano), float(f.nota)))
        return res

    def ordenar_por_titulo(self):
        res = sorted(self.converte_para_lista_tuplas(), key=itemgetter(0))
        return res
    
    def ordenar_por_ano(self):
        res = sorted(self.converte_para_lista_tuplas(), key=itemgetter(1))
        return res
        
    def ordenar_por_nota(self):
        res = sorted(self.converte_para_lista_tuplas(), key=itemgetter(2))
        return res

########## Classe Apresentação ##########
class ListaFilmesView(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Lista de Filmes')
        
        # Variáveis de instância
        self.frames = list()
        self.entradas = dict()
        self.botoes = dict()
        self.objetos = list()
        self.widgets = dict()
        self.variaveis_tk = dict()
        
        self.construtor()

    def construtor(self):
        self.frame_entradas()
        self.frame_ordenar()
        self.frame_treeview()

    def frame_entradas(self): # Frame 1
        entrada = tk.Frame(self, bd=10, relief=tk.SUNKEN)
        entrada.grid(row=0, column=0, sticky='NSWE')
        self.frames.append(entrada)

        titulo_texto = tk.Label(entrada, text='Titulo:')
        titulo_entrada = tk.Entry(entrada, width=30)
        ano_texto = tk.Label(entrada, text='Ano:')
        ano_entrada = tk.Entry(entrada, width=10)
        nota_texto = tk.Label(entrada, text='Nota:')
        nota_entrada = tk.Entry(entrada, width=10)

        titulo_texto.grid(row=0, column=0, sticky='NW')
        titulo_entrada.grid(row=0, column=1, columnspan=3, sticky='NWE')
        ano_texto.grid(row=1, column=0, sticky='NW')
        ano_entrada.grid(row=1, column=1, columnspan=2, sticky='NWE')
        nota_texto.grid(row=1, column=2, sticky='NE')
        nota_entrada.grid(row=1, column=3, columnspan=2, sticky='NWE')

        inserir = tk.Button(entrada, text='Inserir')
        atualizar = tk.Button(entrada, text='Atualizar')
        remover = tk.Button(entrada, text='Remover')
        
        inserir.grid(row=2, column=1, sticky='NWE')
        atualizar.grid(row=2, column=2, sticky='NWE')
        remover.grid(row=2, column=3, sticky='NWE')
        
        self.entradas['titulo_entrada'] = titulo_entrada
        self.entradas['ano_entrada'] = ano_entrada
        self.entradas['nota_entrada'] = nota_entrada
        
        self.botoes['inserir'] = inserir
        self.botoes['atualizar'] = atualizar
        self.botoes['remover'] = remover
        
        l = [titulo_texto, ano_texto, nota_texto,
             titulo_entrada, ano_entrada, nota_entrada,
             inserir, atualizar, remover]
        
        self.objetos.extend(l)

        for obj in self.objetos:
            obj['font'] = ('', 15)

    def frame_ordenar(self): # Frame 2
        ordenar = tk.Frame(self, bd=10, relief=tk.SUNKEN)
        ordenar.grid(row=1, column=0, sticky='NWE')

        ord_texto = tk.Label(ordenar, text='Ordenar por:', font=('', 15))
        ord_texto.grid(row=0, column=0)

        var_ordenacao = tk.StringVar()
        lista_itens = ['titulo', 'ano', 'nota']
        cb = ttk.Combobox(ordenar, textvariable=var_ordenacao, state='readonly', values=lista_itens, font=('', 15))
        cb.grid(row=0, column=1)

        self.widgets['cb'] = cb

        self.variaveis_tk['var_ordenacao'] = var_ordenacao

    def frame_treeview(self): # Frame 3
        treeview = tk.Frame(self, bd=10, relief=tk.RAISED)
        treeview.grid(row=0, column=1, rowspan=2, sticky='NSWE')

        col = ['col0', 'col1', 'col2']
        tit = ['Titulo', 'Ano', 'Nota']
        tam = [200, 40, 40]

        self.widgets['tv'] = TreeView(treeview, col, tit, tam)

########## Classe Controlador ##########
class TreeView:
    def __init__(self, tela, colunas, titulos, tamanhos):
        self.tv = ttk.Treeview(tela, columns=colunas, show='headings')

        for i in range(len(colunas)):
            self.tv.heading(colunas[i], text=titulos[i])
            self.tv.column(colunas[i], width=tamanhos[i]+50, minwidth=tamanhos[i])

        sb_y = ttk.Scrollbar(tela, orient=tk.VERTICAL, command=self.tv.yview)
        self.tv.configure(yscroll=sb_y.set)

        sb_x = ttk.Scrollbar(tela, orient=tk.HORIZONTAL, command=self.tv.xview)
        self.tv.configure(xscroll=sb_x.set)

        self.tv.grid(row=0, column=0)
        sb_y.grid(row=0, column=1, sticky='NS')
        sb_x.grid(row=1, column=0, sticky='WE')

        self.index = list()

    def insere(self, parent, pos, val):
        self.tv.insert(parent, pos, values=val)

    def remove(self):
        tup = self.tv.selection()
        i = tup[0]
        index = self.tv.index(i)
        self.tv.delete(i)
        
        return index

class ListaFilmesController():
    def __init__(self):
        self.model = None
        self.view = None
        
    def inicializa(self, model, view, lista_filmes=None):
        self.model = model
        self.view = view

        self.lista_filmes = lista_filmes
        if lista_filmes:
            for f in lista_filmes._filmes:
                self.view.widgets['tv'].insere('', tk.END, val=[str(f.titulo), int(f.ano), float(f.nota)])

        self._configura()
        
    def _configura(self):
        self.view.botoes['inserir']['command'] = self.insere
        self.view.botoes['atualizar']['command'] = self.atualiza
        self.view.botoes['remover']['command'] = self.remove
        self.view.widgets['cb'].bind('<<ComboboxSelected>>', self.ordena)

    # Gerenciamento dos filmes
    def insere(self):
        t, a, n = self.valores_filme()
        if not self.erro_entrada(t, a, n):
            f = Filme(t, a, n)
            self.view.widgets['tv'].insere('', tk.END, val=[str(t), int(a), float(n)])

            t, a, n = self.valores_entrada()
            self.limpa_entradas(t, a, n)
            self.lista_filmes.insere_filme(f)
            self.view.variaveis_tk['var_ordenacao'].set('')
        
    def remove(self):
        if not self.erro_selecao():
            i = self.view.widgets['tv'].remove()
            self.lista_filmes.remove_filme(i)

    def atualiza(self):
        t, a, n = self.valores_filme()
        if not self.erro_entrada(t, a, n):
            if not self.erro_selecao():
                f = Filme(t, a, n)
                i = self.view.widgets['tv'].remove()
                self.view.widgets['tv'].insere('', i, val=[str(t), int(a), float(n)])

                t, a, n = self.valores_entrada()
                self.limpa_entradas(t, a, n)
                self.lista_filmes.atualiza_filme(i, f)
                self.view.variaveis_tk['var_ordenacao'].set('')

    # métodos auxiliares
    def limpa_entradas(self, titulo, ano, nota):
        titulo.delete(0, len(str(titulo.get())))
        ano.delete(0, len(str(ano.get())))
        nota.delete(0, len(str(nota.get())))

    def valores_filme(self):
        return (
            self.view.entradas['titulo_entrada'].get(),
            self.view.entradas['ano_entrada'].get(),
            self.view.entradas['nota_entrada'].get()
        )

    def valores_entrada(self):
        return (
            self.view.entradas['titulo_entrada'],
            self.view.entradas['ano_entrada'],
            self.view.entradas['nota_entrada']
        )

    # Erros
    def erro_selecao(self):
        if not self.view.widgets['tv'].tv.selection():
            showerror('Erro', 'Selecione um item.')
            return True
        else:
            return False

    def erro_entrada(self, t, a, n):
        s = 'Todos os campos devem estar preenchidos.'
        if t == '':
            s += '\n   - Titulo vazio'
        if a == '':
            s += '\n   - Ano vazio'
        if n == '':
            s += '\n   - Nota vazio'
        if not (t == '' or a == '' or n == ''):
            return False
        showerror('Erro', s)
        return True

    # Ordenação
    def mostra_selecao(self, event):
        s = self.view.variaveis_tk['var_ordenacao'].get()
        showinfo('Ordenação', \
                 f'ordenando por {s}.')

    def ordena(self, event):
        for i in self.view.widgets['tv'].tv.get_children():
            self.view.widgets['tv'].tv.delete(i)

        var = self.view.variaveis_tk['var_ordenacao'].get()
        if var == 'titulo':
            l = self.lista_filmes.ordenar_por_titulo()
        elif var == 'ano':
            l = self.lista_filmes.ordenar_por_ano()
        elif var == 'nota':
            l = self.lista_filmes.ordenar_por_nota()
        
        for f in l:
            self.view.widgets['tv'].insere('', tk.END, val=[str(f[0]), int(f[1]), float(f[2])])
        # self.mostra_selecao(event)

def main():
    f1 = Filme('O resgate do soldado Ryan', 1998, 9.0)
    f2 = Filme('A vida é bela', 1997, 9.5)
    f3 = Filme('Avengers: ultimato', 2019, 10.0)
    
    lf = ListaFilmesModel()
    
    # Adiciona alguns filmes e imprime lista
    lf.insere_filme(f1)
    lf.insere_filme(f2)
    lf.insere_filme(f3)
    print(lf.converte_para_lista())
    
    # Atualiza primeiro filme da lista
    novo_f1 = Filme('O resgate do soldado Ryan', 1998, 8.5)
    lf.atualiza_filme(0, novo_f1)
    print(lf.converte_para_lista())
    
    # Remove o filme da posição 1 na lista
    lf.remove_filme(1)
    print(lf.converte_para_lista())
    
    controller = ListaFilmesController()
    model = ListaFilmesModel()
    view = ListaFilmesView()
    
    controller.inicializa(model, view, lf)
    view.mainloop()
    
if __name__ == '__main__':
    main()