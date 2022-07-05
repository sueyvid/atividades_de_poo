import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showerror, showinfo

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

########## Classe Apresentação ##########
lista_itens = None
lb = None

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

    def frame_ordenar(self): # Frame 1.2
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

    def frame_treeview(self): # Frame 2
        treeview = tk.Frame(self, bd=10, relief=tk.RAISED)
        treeview.grid(row=0, column=1, rowspan=2, sticky='NSWE')

        nomes_colunas = ['col0', 'col1', 'col2']
        tv = ttk.Treeview(treeview, columns=nomes_colunas, show='headings')

        tv.heading('col0', text='Titulo')
        tv.heading('col1', text='Ano')
        tv.heading('col2', text='Nota')

        tv.column('col0', width=200, minwidth=210)
        tv.column('col1', width=40, minwidth=50)
        tv.column('col2', width=40, minwidth=50)

        sb_y = ttk.Scrollbar(treeview, orient=tk.VERTICAL, command=tv.yview)
        tv.configure(yscroll=sb_y.set)

        sb_x = ttk.Scrollbar(treeview, orient=tk.HORIZONTAL, command=tv.xview)
        tv.configure(xscroll=sb_x.set)

        self.widgets['tv'] = tv

        tv.grid(row=0, column=0)
        sb_y.grid(row=0, column=1, sticky='NS')
        sb_x.grid(row=1, column=0, sticky='WE')

########## Classe Controlador ##########
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
                self.view.widgets['tv'].insert('', tk.END, values=[f.titulo, f.ano, f.nota])

        self._configura()
        
    def _configura(self):
        self.view.botoes['inserir']['command'] = self.insere
        self.view.botoes['atualizar']['command'] = self.atualiza
        self.view.botoes['remover']['command'] = self.remove
        self.view.widgets['cb'].bind('<<ComboboxSelected>>', self.mostra_selecao)

    def mostra_selecao(self, event):
        s = self.view.variaveis_tk['var_ordenacao'].get()
        showinfo('Ordenacao', \
                 f'ordenando por {s}.')

    def limpa_entradas(self, titulo, ano, nota):
        titulo.delete(0, len(str(titulo.get())))
        ano.delete(0, len(str(ano.get())))
        nota.delete(0, len(str(nota.get())))

    def insere(self):
        t = self.view.entradas['titulo_entrada'].get()
        a = self.view.entradas['ano_entrada'].get()
        n = self.view.entradas['nota_entrada'].get()
        
        if t is '' or a is '' or n is '':
            showerror('Erro', \
                      'Todos os campos devem estar preenchidos.')
        else:
            f = Filme(t, a, n)
            self.view.widgets['tv'].insert('', tk.END, values=[t, a, n])

            t = self.view.entradas['titulo_entrada']
            a = self.view.entradas['ano_entrada']
            n = self.view.entradas['nota_entrada']
            self.limpa_entradas(t, a, n)
            self.lista_filmes.insere_filme(f)
        
    def remove(self):
        tup = self.view.widgets['tv'].selection()
        i = tup[0]
        self.view.widgets['tv'].delete(i)

        i = int(tup[0][-1]) - 1
        self.lista_filmes.remove_filme(i)

    def atualiza(self):
        t = self.view.entradas['titulo_entrada'].get()
        a = self.view.entradas['ano_entrada'].get()
        n = self.view.entradas['nota_entrada'].get()
        f = Filme(t, a, n)
        tup = self.view.widgets['tv'].selection()
        i = tup[0]
        self.view.widgets['tv'].delete(i)
        i = int(tup[0][-1]) - 1
        self.view.widgets['tv'].insert('', i, values=[t, a, n])
        
        t = self.view.entradas['titulo_entrada']
        a = self.view.entradas['ano_entrada']
        n = self.view.entradas['nota_entrada']
        self.limpa_entradas(t, a, n)
        print(i)
        self.lista_filmes.atualiza_filme(i, f)
        print(self.lista_filmes.converte_para_lista())

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