from obra import Obra
from museu import Museu

def main():
    dados_obras = [('mona lisa', 'da vinci', 1797), ('a noite estrelada', 'van gogh', 1889),
                   ('guernica', 'picasso', 1937), ('a persistencia da memoria', 'dali', 1931)]
    
    # cria museu
    m = Museu('museu magnifico', dados_obras)

    # imprime obras
    m.imprime_obras()

    # remove obras do museu
    m.remove_obra('a ultima ceia') # nao faz nada
    m.remove_obra('guernica')

    # imprime obras
    m.imprime_obras()

    # obra 'guernica' foi removida da memória
    
if __name__ == "__main__":
    main()