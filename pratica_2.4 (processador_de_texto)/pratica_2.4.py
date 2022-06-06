class PreProcessador:
    def __init__(self, texto):
        self._texto = texto
        self._lista_palavras = list()

    def processa(self):
        self._lista_palavras = self._texto.lower().split()
        for i, palavra in enumerate(self._lista_palavras):
            if not palavra[-1].isalpha():
                self._lista_palavras[i] = palavra[0:-1]
    
    def __str__(self):
        r = '('
        for palavra in self._lista_palavras:
            r += palavra
            r += ', '
        r += ')'
        return r

class ContadorPalavras(PreProcessador):
    def __init__(self, texto):
        super().__init__(texto)
        self._ocorrencias = dict()
    
    def processa(self):
        PreProcessador.processa(self)
        for palavra in self._lista_palavras:
            if palavra not in self._ocorrencias:
                self._ocorrencias[palavra] = self._lista_palavras.count(palavra)
    
    def __str__(self):
        r = 'Frequência das palavras:\n'
        for key in self._ocorrencias:
            r += ('{}: {} vezes\n'.format(key, self._ocorrencias.get(key)))
        return r

class Tradutor(PreProcessador):
    def __init__(self, texto):
        super().__init__(texto)
        self._traducoes = {'olá': 'hello', 'este': 'this', 'é': 'is',
                           'um': 'one', 'exemplo': 'example', 'de': 'of',
                           'texto': 'text', 'com': 'with', 'termos': 'terms',
                           'repetidos': 'repeated', 'possui': 'has', 'vários': 'various'}
        self._lista_palavras_trad = list()
    
    def processa(self):
        PreProcessador.processa(self)
        for palavra in self._lista_palavras:
            self._lista_palavras_trad.append(self._traducoes[palavra])
    
    def __str__(self):
        r = 'Tradução robótica:\n'
        for palavra in self._lista_palavras_trad:
            r += f'{palavra} '
        return r

class ProcessadorTexto(ContadorPalavras, Tradutor):
    def __init__(self, texto):
        super().__init__(texto)
    
    def processa(self):
        ContadorPalavras.processa(self)
        print(ContadorPalavras.__str__(self))
        Tradutor.processa(self)
        print(Tradutor.__str__(self))

if __name__ == '__main__':
    # Descomente a seguir para testar apenas a classe PreProcessador
    # preprocessador = PreProcessador('OLá! Este é um exemplo de texto com termos repetidos.'
    #                                 ' Este texto possui vários termos repetidos:'
    #                                 ' este, Este, ESte, esTE!')
    # preprocessador.processa()
    # print(preprocessador)

    # Descomente a seguir para testar apenas a classe ContadorPalavras
    # contador = ContadorPalavras('OLá! Este é um exemplo de texto com termos repetidos.'
    #                             ' Este texto possui vários termos repetidos:'
    #                             ' este, Este, ESte, esTE!')
    # contador.processa()
    # print(contador)

    # Descomente a seguir para testar apenas a classe Tradutor
    # tradutor = Tradutor('OLá! Este é um exemplo de texto com termos repetidos.'
    #                     ' Este texto possui vários termos repetidos:'
    #                     ' este, Este, ESte, esTE!')
    # tradutor.processa()
    # print(tradutor)

    processadortexto = ProcessadorTexto('OLá! Este é um exemplo de texto com termos repetidos.'
                                        ' Este texto possui vários termos repetidos:'
                                        ' este, Este, ESte, esTE!')
    processadortexto.processa()