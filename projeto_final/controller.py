from setuptools import Command
from Excecoes import *
from interface import *
from modelo import *
from data import *
from pandas.errors import ParserError

class Controller:
    def __init__(self):
        self.view = None
        self.model = None

        self.lista = None
        self.fila = None
        self.qtd_mostrando = 0
        self.arquivo = None
        self.scroll_y_position = None
        self.ordenacao = None

    def inicia(self, view):
        self.view = view
        self._configura()
        
    def _configura(self):
        bt_resetar = self.view.botoes['resetar']
        bt_resetar.command(self.resetar)

        bt_pesquisar = self.view.botoes['pesquisar']
        bt_pesquisar.command(self.pesquisar)

        bt_importar_dados = self.view.botoes['importar']
        bt_importar_dados.command(self.importar_dados)

        bt_mostrar_grafico = self.view.botoes['grafico']
        bt_mostrar_grafico.command(self.mostrar_grafico)

        bt_mostrar_mais = self.view.botoes['mais']
        bt_mostrar_mais.command(self.adiciona_na_lista)

        # Ordenação
        self.ordenacao = tk.StringVar()
        self.crescente = tk.BooleanVar(value=False)
        self.view.tv.heading('col0', command=lambda:self.ordena('titulo'))
        self.view.tv.heading('col1', command=lambda:self.ordena('canal'))
        self.view.tv.heading('col2', command=lambda:self.ordena('views'))
        self.view.tv.heading('col3', command=lambda:self.ordena('likes'))

        # Scroll da tabela
        scroll_y = self.view.widgets['scroll_y']
        scroll_y.bind('<MouseWheel>', self.confere_valor_scroll)
        self.view.tv.bind('<MouseWheel>', self.confere_valor_scroll)
        self.view.bind('<Motion>', self.confere_valor_scroll)
        self.scroll_y_position = tk.StringVar()

        cb = self.view.widgets['cb']
        cb.bind('<<ComboboxSelected>>', self.cb_opcao)

    def cb_opcao(self, event=None):
        cb = self.view.widgets['cb']
        l5 = self.view.widgets['tipo_pesquisa']
        l5.texto = ''

        if cb.texto == '':
            l5.texto = 'Escolha o tipo de pesquisa...'
        if cb.texto == 'titulo':
            l5.texto = 'Digite o título na barra de pesquisa.'
        if cb.texto == 'canal':
            l5.texto = 'Digite o nome do canal na barra de pesquisa.'
        if cb.texto == 'periodo':
            l5.texto = 'Digite: "dd/mm/aaaa - dd/mm/aaaa"'
        if cb.texto == 'categoria':
            s = 'Digite uma das categorias:\n'
            for i in self.model.categorias:
                s += f'{i}\n'
            l5.texto = s

    def reseta_ordenacoes(self):
        self.view.tv.heading('col0', text='Titulo')
        self.view.tv.heading('col1', text='Canal')
        self.view.tv.heading('col2', text='Views')
        self.view.tv.heading('col3', text='Likes')

    def ordena(self, tipo):
        if self.arquivo:
            self.reseta_ordenacoes()
            if not self.crescente.get():
                if tipo == 'titulo':
                    self.ordenacao.set('titulo')
                    self.lista.sort(key=lambda x: x.titulo)
                    self.view.tv.heading('col0', text='Titulo 🔽')
                elif tipo == 'canal':
                    self.ordenacao.set('canal')
                    self.lista.sort(key=lambda x: x.canal)
                    self.view.tv.heading('col1', text='Canal 🔽')
                elif tipo == 'views':
                    self.ordenacao.set('views')
                    self.lista.sort(key=lambda x: x.cont_views)
                    self.view.tv.heading('col2', text='Views 🔽')
                elif tipo == 'likes':
                    self.ordenacao.set('likes')
                    self.lista.sort(key=lambda x: x.likes)
                    self.view.tv.heading('col3', text='Likes 🔽')
                self.crescente.set(True)
            else:
                if tipo == 'titulo':
                    self.ordenacao.set('titulo')
                    self.lista.sort(key=lambda x: x.titulo)
                    self.view.tv.heading('col0', text='Titulo 🔼')
                elif tipo == 'canal':
                    self.ordenacao.set('canal')
                    self.lista.sort(key=lambda x: x.canal)
                    self.view.tv.heading('col1', text='Canal 🔼')
                elif tipo == 'views':
                    self.ordenacao.set('views')
                    self.lista.sort(key=lambda x: x.cont_views)
                    self.view.tv.heading('col2', text='Views 🔼')
                elif tipo == 'likes':
                    self.ordenacao.set('likes')
                    self.lista.sort(key=lambda x: x.likes)
                    self.view.tv.heading('col3', text='Likes 🔼')
                self.lista.reverse()
                self.crescente.set(False)
            self.fila = self.lista.copy()
            self.view.tv.limpa()
            self.qtd_mostrando = 0
            self.adiciona_na_lista()

    def confere_valor_scroll(self, event=None):
        if self.arquivo:
            scroll_y = self.view.widgets['scroll_y'].get()
            self.scroll_y_position.set(scroll_y[1])
            if self.scroll_y_position.get() == '1.0':
                self.adiciona_na_lista()

    def resetar(self):
        cb = self.view.widgets['cb']
        cb.texto = ''
        pesquisa = self.view.widgets['barra_pesquisa']
        pesquisa.texto = ''
        rb = self.view.widgets['rb']
        rb.texto = ''
        tipo_pesquisa = self.view.widgets['tipo_pesquisa']
        tipo_pesquisa.texto = 'Escolha o tipo de pesquisa...'
        if self.arquivo:
            self.insere_dados()

    def mostrar_grafico(self):
        rb = self.view.widgets['rb']
        try:
            if not self.arquivo:
                raise ArquivoNaoSelecionado()
            if rb.texto == '':
                raise OpcaoNaoSelecionada('Algum dos tipos de gráficos deve ser selecionado.')
            if rb.texto == 'assistidos':
                self.model.mostra_mais_assistidos()
            if rb.texto == 'likes':
                self.model.mostra_mais_likes()
            if rb.texto == 'comentários':
                self.model.mostra_mais_comentarios()
        except ArquivoNaoSelecionado:
            ErroArquivoNaoSelecionado()
        except OpcaoNaoSelecionada as err:
            ErroOpcaoNaoSelecionada(err)
        except ExcecaoSistema:
            ErroInesperado()
        
    def importar_dados(self):
        tipo_de_arq = ExploradorDeArquivo.tipos_arq
        exp_arquivo = ExploradorDeArquivo(tipo_de_arq)
        nome_do_arq = exp_arquivo.texto
        try:
            if not exp_arquivo.texto:
                raise ArquivoNaoSelecionado()
            m = BancoDadosYT(nome_do_arq)
            self.model = m
            self.arquivo = exp_arquivo
            exibe_nome_arquivo = self.view.widgets['arquivo']
            exibe_nome_arquivo.texto = nome_do_arq
            self.insere_dados()
        except ArquivoNaoSelecionado:
            AvisoArquivoNaoSelecionado()
        except ParserError:
            ErroArquivoGrande()
        except ExcecaoSistema:
            ErroInesperado()

    def pesquisar(self):
        pesquisa = self.view.widgets['barra_pesquisa'].get()
        cb = self.view.widgets['cb']
        try:
            if not self.arquivo:
                raise ArquivoNaoSelecionado()
            if pesquisa == '':
                raise PesquisaVazio()
            if cb.texto == '':
                raise OpcaoNaoSelecionada('Algum dos tipos de pesquisa deve ser selecionado.')
            self.insere_dados()
        except ArquivoNaoSelecionado:
            ErroArquivoNaoSelecionado()
        except PesquisaVazio:
            ErroPesquisaVazio()
        except OpcaoNaoSelecionada as err:
            ErroOpcaoNaoSelecionada(err)
        except:
            ErroInesperado()

    def insere_dados(self):
        self.reseta_ordenacoes()
        cb = self.view.widgets['cb']
        pesquisa = self.view.widgets['barra_pesquisa'].get()
        try:
            if not self.arquivo:
                raise ArquivoNaoSelecionado()
            if cb.texto == '':
                res = self.model.todos()
            if cb.texto == 'titulo':
                res = self.model.busca_por_titulo(pesquisa)
            if cb.texto == 'canal':
                res = self.model.busca_por_canal(pesquisa)
            if cb.texto == 'categoria':
                res = self.model.busca_por_categoria(pesquisa)
            if cb.texto == 'periodo':
                p = Periodo(pesquisa)
                di = p.data_inicial()
                df = p.data_final()
                res = self.model.busca_por_periodo(di, df)
            if not res:
                raise NadaEncontrado()
            self.qtd_mostrando = 0
            self.view.tv.limpa()
            self.lista = res
            self.fila = res.copy()
            self.adiciona_na_lista()
            exibe_tam_lista = self.view.widgets['tam_lista']
            exibe_tam_lista.texto = f'Tamanho da lista: {len(res)}'
        except ArquivoNaoSelecionado:
            ErroArquivoNaoSelecionado()
        except NadaEncontrado:
            AvisoNenhumResultado()
        except:
            ErroInesperado()

    def adiciona_na_lista(self):
        lista = self.fila
        try:
            if not self.arquivo:
                raise ArquivoNaoSelecionado
            for i in range(len(lista)):
                if i < 5:
                    video = lista[i]
                    l = [video.titulo, video.canal, video.cont_views, video.likes]
                    self.view.tv.insere('', tk.END, values=l)
                    self.qtd_mostrando += 1
            for i in range(len(lista)):
                if i < 5:
                    lista.pop(0)
            n = self.qtd_mostrando
            exibe_mostrando = self.view.widgets['mostrando']
            exibe_mostrando.texto = f'Mostrando: {n}'
        except ArquivoNaoSelecionado:
            ErroArquivoNaoSelecionado()
        except:
            ErroInesperado()
    
def main():
    v = BuscadorDeVideos()
    c = Controller()
    c.inicia(v)
    v.mainloop()

if __name__ == '__main__':
    main()