from tkinter.messagebox import showerror, showinfo

class ExcecaoSistema(Exception):
    '''Classe de exceções do sistema'''
    pass

class GraficoSelecao(ExcecaoSistema):
    '''
    Erro quando não houver nenhuma
    opção selecionada para exibição
    do gráfico
    '''
    pass

class ArquivoNaoSelecionado(ExcecaoSistema):
    '''
    Erro quando nenhum arquivo foi
    selecionado no explorador de arquivos
    '''
    pass

def ErroGraficoSelecao():
    showerror('Tipo de gráfico não selecionado', 'Algum dos tipos de gráficos deve ser selecionado.')

def ErroArquivoNaoSelecionado():
    showerror('Arquivo não selecionado', 'Nenhum arquivo foi selecionado para leitura.')

def AvisoArquivoNaoSelecionado():
    showinfo('Nenhum arquivo selecionado', 'Nenhum arquivo foi selecionado no explorador de arquivos.')

def ErroPesquisaVazio():
    showerror('Nada a pesquisar', 'A caixa de pesquisa está vazia. Digite algo.')

def AvisoSemResultados():
    showinfo('Nenhum resultado', 'Nenhum resultado foi encontrado para a pesquisa.')

def ErroTipoDePesquisa():
    showerror('Nenhum tipo de pesquisa selecionado', 'Selecione o tipo de pesquisa que deseja fazer.')