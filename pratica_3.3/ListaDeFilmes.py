import tkinter as tk

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
        self.widgets = list()
        self.entradas = dict()
        self.botoes = dict()
        self.objetos = list()
        
        self.construtor()

    def construtor(self):
        self.widget_entradas()
        self.widget_lista()

    def widget_entradas(self): # Frame 1
        entrada = tk.Frame(self, bd=10, relief=tk.SUNKEN)
        entrada.grid(row=0, column=0, sticky='NWE')
        self.widgets.append(entrada)

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

    def widget_lista(self): # Frame 2
        lista = tk.Frame(self, bd=10, relief=tk.RAISED)
        lista.grid(row=0, column=1, sticky='NSWE')
        self.widgets.append(lista)

        self.columnconfigure(1, weight=1)
        lista.columnconfigure(0, weight=1)

        global lista_itens, lb
    
        v_lista_itens = tk.StringVar()
        v_lista_itens.set(lista_itens.converte_para_lista())
        
        lb = tk.Listbox(lista, listvariable=v_lista_itens, font=('', 15), width=41, height=21)
        lb.grid(row=0, column=0, sticky='NSWE')

########## Classe Controlador ##########
class ListaFilmesController():
    def __init__(self):
        self.model = None
        self.view = None
        
    def inicializa(self, model, view):
        self.model = model
        self.view = view
        self._configura()
        
    def _configura(self):
        self.view.botoes['inserir']['command'] = lambda: ListaFilmesController.inseri(self.view.entradas['titulo_entrada'], self.view.entradas['ano_entrada'], self.view.entradas['nota_entrada'])
        self.view.botoes['atualizar']['command'] = lambda: ListaFilmesController.atualiza(self.view.entradas['titulo_entrada'], self.view.entradas['ano_entrada'], self.view.entradas['nota_entrada'])
        self.view.botoes['remover']['command'] = lambda: ListaFilmesController.remove()
        
    def cria_filme(titulo, ano, nota):
        t = titulo.get()
        a = ano.get()
        n = nota.get()
        return Filme(t, a, n)

    def limpa_entradas(titulo, ano, nota):
        titulo.delete(0, len(str(titulo.get())))
        ano.delete(0, len(str(ano.get())))
        nota.delete(0, len(str(nota.get())))

    def inseri(titulo, ano, nota):
        global lista_itens, lb
        print('inserindo')
        
        f = ListaFilmesController.cria_filme(titulo, ano, nota)
        ListaFilmesController.limpa_entradas(titulo, ano, nota)
        
        ListaFilmesModel.insere_filme(lista_itens, f)
        lb.insert(len(lista_itens.converte_para_lista()), str(f))
        
    def remove():
        global lista_itens, lb
        
        tup = lb.curselection() # obtém tupla com todos os índices do listbox que estão selecionados
        i = tup[0] # obtém o índice do item selecionado
        ListaFilmesModel.remove_filme(lista_itens, i)
        lb.delete(i)

    def atualiza(titulo, ano, nota):
        global lista_itens, lb
        
        f = ListaFilmesController.cria_filme(titulo, ano, nota)
        ListaFilmesController.limpa_entradas(titulo, ano, nota)
        
        tup = lb.curselection() # obtém tupla com todos os índices do listbox que estão selecionados
        i = tup[0] # obtém o índice do item selecionado
        ListaFilmesModel.atualiza_filme(lista_itens, i, f)
        lb.delete(i)
        lb.insert(i, str(f))

def main():
    global lista_itens, lb

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

    lista_itens = lf
    
    controller = ListaFilmesController()
    model = ListaFilmesModel()
    view = ListaFilmesView()
    
    controller.inicializa(model, view)
    view.mainloop()
    
if __name__ == '__main__':
    main()