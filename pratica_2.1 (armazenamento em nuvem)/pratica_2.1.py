class InfoArquivo:
    _formatos_suportados = ['txt', 'pdf', 'jpg', 'zip', 'mp4']    
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho

    def __str__(self):
        return f'Arquivo: {self.nome} ({self.tamanho} MB)'

    def excede_tamanho(self):
        if self.tamanho > 1000:
            return True
        else:
            return False

    @staticmethod
    def imprime_arquivos_suportados():
        print(20*'-')
        print('Formatos suportados:')
        for formato in InfoArquivo._formatos_suportados:
            print(formato)
        print(20*'-')

class InfoImagem(InfoArquivo):
    def __init__(self, nome, tamanho, resolucao):
        super().__init__(nome, tamanho)
        self.resolucao = resolucao
    
    def __str__(self):
        return f'Imagem: {self.nome}, resolucao: {self.resolucao} ({self.tamanho} MB)'

    def redimensiona(self):
        self.resolucao[0] /= 2
        self.resolucao[1] /= 2

class InfoVideo(InfoImagem):
    def __init__(self, nome, tamanho, resolucao, duracao):
        super().__init__(nome, tamanho, resolucao)
        self.duracao = duracao

    def __str__(self):
        return f'Video: {self.nome}, resolucao: {self.resolucao}, duracao: {self.duracao} ({self.tamanho} MB)'

    def excede_tamanho(self):
        super().excede_tamanho()
        if self.resolucao[0] > 3840:
            return True
        else:
            return False

def main():
    a1 = InfoArquivo('anotacoes.txt', 0.01)
    a2 = InfoArquivo('nota_fiscal.pdf', 2.0)
    a3 = InfoArquivo('arquivo.zip', 1500)
    i1 = InfoImagem('foto1.jpg', 3.0, [3000, 2000])
    i2 = InfoImagem('foto2.jpg', 3.0, [3000, 2000])
    v1 = InfoVideo('video1.mp4', 50.0, [1920, 1080], 3602)
    v2 = InfoVideo('video2.mp4', 20.0, [3840, 2060], 300)
    v3 = InfoVideo('video3.mp4', 65.0, [7680, 4320], 20)

    # Insira aqui a chamada ao método de classe que
    # imprime os formatos de arquivos suportados
    InfoArquivo.imprime_arquivos_suportados()

    diretorio = [a1, a2, a3, i1, i2, v1, v2, v3]

    print('\n>>>>>>>>>>>>>>>>>>>>>')
    print('Antes do redimensionamento:')
    for a in diretorio:
        print(a) # chama o __str__ de acordo com a classe
        print(a.excede_tamanho())

    diretorio.remove(a3)
    i2.redimensiona()
    v3.redimensiona()

    print('\n>>>>>>>>>>>>>>>>>>>>>')
    print('Depois do redimensionamento:')
    for a in diretorio:
        print(a)
        print(a.excede_tamanho())

if __name__ == '__main__':
    main()