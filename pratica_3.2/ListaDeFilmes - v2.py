import tkinter as tk

########## Classes dadas ##########
class Filme:
    def __init__(self, tit, ano, nota):
        self.titulo = tit
        self.ano = ano
        self.nota = nota

    def __str__(self):
        return f'{self.titulo} ({self.ano}) - {self.nota}'

class ListaFilmes:
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

########## Código da atividade ##########
lista_itens = None
lb = None

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.widgets = list()
        self.objetos_entrada = list()
        self.construtor()

    def construtor(self):
        self.widget_entradas()
        self.widget_pesquisa()
        self.widget_lista()
        self.config()

    def config(self):
        for obj in self.objetos_entrada:
            obj['font'] = ('', 15)

    def widget_entradas(self): # Frame 1
        entrada = tk.Frame(self, bd=10, relief=tk.SUNKEN)
        entrada.grid(row=0, column=0, rowspan=2, sticky='NWE')
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

        inserir = tk.Button(entrada, text='Inserir', command=lambda: Logica.inseri(titulo_entrada, ano_entrada, nota_entrada))
        atualizar = tk.Button(entrada, text='Atualizar', command=lambda: Logica.atualiza(titulo_entrada, ano_entrada, nota_entrada))
        remover = tk.Button(entrada, text='Remover', command=lambda: Logica.remove())
        
        inserir.grid(row=2, column=1, sticky='NWE')
        atualizar.grid(row=2, column=2, sticky='NWE')
        remover.grid(row=2, column=3, sticky='NWE')

        l = [titulo_texto, titulo_entrada, ano_texto,
             ano_entrada, nota_texto, nota_entrada,
             inserir, atualizar, remover]

        self.objetos_entrada.extend(l)

    def widget_pesquisa(self):
        pesquisa = tk.Frame(self, bd=10, relief=tk.SUNKEN)
        pesquisa.grid(row=1, column=1, sticky='SWE')
        self.widgets.append(pesquisa)

        pesquisa_texto = tk.Label(pesquisa, text='Titulo:')
        pesquisa_texto.grid(row=0, column=0, sticky='NSW')

        pesquisa_entrada = tk.Entry(pesquisa)
        pesquisa_entrada.grid(row=0, column=1, sticky='NSWE')

        pesquisa_botao = tk.Button(pesquisa, text='Pesquisar', command=lambda: Logica.pesquisa(pesquisa_entrada))
        pesquisa_botao.grid(row=0, column=2, sticky='NE')

        l = [pesquisa_texto, pesquisa_entrada, pesquisa_botao]

        self.objetos_entrada.extend(l)

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

class Logica():
    def cria_filme(titulo, ano, nota):
        t = titulo.get()
        a = ano.get()
        n = nota.get()
        return Filme(t, a, n)

    def pesquisa(entrada):
        global lista_itens, lb

        lb.select_clear(0, len(lista_itens.converte_para_lista()))
        titulo = entrada.get()
        i = 0
        for filme in lista_itens.converte_para_lista():
            if titulo.lower() in filme.lower():
                lb.select_set(i)
            i += 1

        entrada.delete(0, len(str(titulo)))

    def limpa_entradas(titulo, ano, nota):
        titulo.delete(0, len(str(titulo.get())))
        ano.delete(0, len(str(ano.get())))
        nota.delete(0, len(str(nota.get())))

    def inseri(titulo, ano, nota):
        global lista_itens, lb
        
        f = Logica.cria_filme(titulo, ano, nota)
        Logica.limpa_entradas(titulo, ano, nota)
        
        ListaFilmes.insere_filme(lista_itens, f)
        lb.insert(len(lista_itens.converte_para_lista()), str(f))
        
    def remove():
        global lista_itens, lb
        
        tup = lb.curselection() # obtém tupla com todos os índices do listbox que estão selecionados
        # i = tup[0] # obtém o índice do item selecionado
        for i in reversed(tup):
            ListaFilmes.remove_filme(lista_itens, i)
            lb.delete(i)

    def atualiza(titulo, ano, nota):
        global lista_itens, lb
        
        f = Logica.cria_filme(titulo, ano, nota)
        Logica.limpa_entradas(titulo, ano, nota)
        
        tup = lb.curselection() # obtém tupla com todos os índices do listbox que estão selecionados
        # i = tup[0] # obtém o índice do item selecionado
        for i in reversed(tup):
            ListaFilmes.atualiza_filme(lista_itens, i, f)
            lb.delete(i)
            lb.insert(i, str(f))

def main():
    global lista_itens, lb

    f1 = Filme('O resgate do soldado Ryan', 1998, 9.0)
    f2 = Filme('A vida é bela', 1997, 9.5)
    f3 = Filme('Avengers: ultimato', 2019, 10.0)
    
    lf = ListaFilmes()
    
    # Adiciona alguns filmes e imprime lista
    lf.insere_filme(f1)
    lf.insere_filme(f2)
    lf.insere_filme(f3)
    # print(lf.converte_para_lista())
    
    # Atualiza primeiro filme da lista
    novo_f1 = Filme('O resgate do soldado Ryan', 1998, 8.5)
    lf.atualiza_filme(0, novo_f1)
    # print(lf.converte_para_lista())
    
    # Remove o filme da posição 1 na lista
    lf.remove_filme(1)
    # print(lf.converte_para_lista())

    lista_itens = lf

    tela = Interface()
    tela.title('Lista de Filmes')
    tela.mainloop()
    
if __name__ == '__main__':
    main()