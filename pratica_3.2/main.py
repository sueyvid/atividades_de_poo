import tkinter as tk

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

lista_itens = None
lb = None
MinhaLista = ListaFilmes()

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
    global lista_itens, lb, MinhaLista
    
    f = cria_filme(titulo, ano, nota)
    limpa_entradas(titulo, ano, nota)
    
    ListaFilmes.insere_filme(MinhaLista, f)
    lista_itens.append(str(f))
    lb.insert(len(lista_itens), str(f))
    
def remove():
    global lista_itens, lb
    
    tup = lb.curselection() # obtém tupla com todos os índices do listbox que estão selecionados
    i = tup[0] # obtém o índice do item selecionado
    ListaFilmes.remove_filme(MinhaLista, i)
    lista_itens.pop(i)
    lb.delete(i)

def atualiza(titulo, ano, nota):
    global lista_itens, lb
    
    f = cria_filme(titulo, ano, nota)
    limpa_entradas(titulo, ano, nota)
    
    tup = lb.curselection() # obtém tupla com todos os índices do listbox que estão selecionados
    i = tup[0] # obtém o índice do item selecionado
    ListaFilmes.atualiza_filme(MinhaLista, i, f)
    lista_itens.pop(i)
    lista_itens.insert(i, str(f))
    lb.delete(i)
    lb.insert(i, str(f))

def config(nl, nc, tela):
    for i in range(nl):
        tela.rowconfigure(i, weight=1)
    for j in range(nc):
        tela.columnconfigure(j, weight=1)

def main():
    tela = tk.Tk()
    tela.title('Lista de Filmes')
    
    entrada = tk.Frame(tela, bd=10, relief=tk.SUNKEN)
    entrada.grid(row=0, column=0, sticky='NSWE')
    lista = tk.Frame(tela, bd=10, relief=tk.RAISED)
    lista.grid(row=0, column=1, sticky='NSWE')
    config(0, 2, tela)
    
    titulo_texto = tk.Label(entrada, text='Titulo:')
    titulo_texto.grid(row=0, column=0, sticky='NW')
    titulo_entrada = tk.Entry(entrada, width=30)
    titulo_entrada.grid(row=0, column=1, columnspan=3, sticky='NWE')
    ano_texto = tk.Label(entrada, text='Ano:')
    ano_texto.grid(row=1, column=0, sticky='NW')
    ano_entrada = tk.Entry(entrada, width=10)
    ano_entrada.grid(row=1, column=1, columnspan=2, sticky='NWE')
    nota_texto = tk.Label(entrada, text='Nota:')
    nota_texto.grid(row=1, column=2, sticky='NE')
    nota_entrada = tk.Entry(entrada, width=10)
    nota_entrada.grid(row=1, column=3, columnspan=2, sticky='NWE')
    
    inserir = tk.Button(entrada, text='Inserir', command=lambda: inseri(titulo_entrada, ano_entrada, nota_entrada))
    inserir.grid(row=2, column=1, sticky='NWE')
    atualizar = tk.Button(entrada, text='Atualizar', command=lambda: atualiza(titulo_entrada, ano_entrada, nota_entrada))
    atualizar.grid(row=2, column=2, sticky='NWE')
    remover = tk.Button(entrada, text='Remover', command=lambda: remove())
    remover.grid(row=2, column=3, sticky='NWE')
    
    entrada.columnconfigure(1, weight=1)
    entrada.columnconfigure(2, weight=1)
    entrada.columnconfigure(3, weight=1)
    
    l = [titulo_texto, titulo_entrada, ano_texto, ano_entrada, nota_texto, nota_entrada, inserir, atualizar, remover]
    for obj in l:
        obj['font'] = ('', 15)
        
    global lista_itens, lb
    
    lista_itens = list()
    v_lista_itens = tk.StringVar()
    v_lista_itens.set(lista_itens)
    
    lb = tk.Listbox(lista, listvariable=v_lista_itens, font=('', 15), width=51, height=21)
    lb.grid(row=0, column=0, sticky='NSWE')
    
    tela.mainloop()
    
if __name__ == '__main__':
    main()