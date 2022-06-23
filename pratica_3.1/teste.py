from main import *

def main():
    l1 = Livro()
    l2 = Livro()
    l1.codigo = 123456
    l2.codigo = 234567
    l3 = Livro()
    bib = Biblioteca('BCZM')
    book = int
    bib.cadastrar(l1)
    bib.cadastrar(l1)
    # for c in Livro.ISBN:
    #     print(c)

if __name__ == '__main__':
    main()