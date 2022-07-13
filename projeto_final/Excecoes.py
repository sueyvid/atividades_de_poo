from tkinter.messagebox import showerror, showinfo

class ExcecaoSistema(Exception):
    '''Classe de exceções do sistema'''
    pass

class OpcaoNaoSelecionada(ExcecaoSistema):
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

class PesquisaVazio(ExcecaoSistema):
    '''
    Erro quando se tenta pesquisar sem ter
    digitado nada na caixa de busca
    '''
    pass

class NadaEncontrado(ExcecaoSistema):
    '''
    Erro quando nenhum dado com os valores
    passados é encontrado
    '''
    pass

def ErroArquivoNaoSelecionado():
    showerror('Arquivo não selecionado', 'Nenhum arquivo foi selecionado para leitura.')

def ErroOpcaoNaoSelecionada(text):
    showerror('Nenhuma opção foi selecionada', text)

def ErroPesquisaVazio():
    showerror('Nada a pesquisar', 'A caixa de pesquisa está vazia. Digite algo.')

def ErroArquivoGrande():
    showerror('Arquivo grande', 'Arquivo muito grande para ser aberto pelo programa.')

def ErroPeriodoIncorreto():
    showerror('Perído incorreto', 'Você digitou o perído de forma incorreta tente no formato: "dd/mm/aaaa - dd/mm/aaaa"')

def AvisoArquivoNaoSelecionado():
    showinfo('Nenhum arquivo selecionado', 'Nenhum arquivo foi selecionado no explorador de arquivos.')

def AvisoNenhumResultado():
    showinfo('Nenhum resultado', 'Nenhum resultado foi encontrado para a pesquisa.')

def ErroNoSistema():
    showerror('Erro inesperado', 'Ops! Ocorreu um erro no sistema.')

def ErroInesperado():
    showerror('Erro inesperado', 'Ops! Ocorreu um erro fora do sistema.')