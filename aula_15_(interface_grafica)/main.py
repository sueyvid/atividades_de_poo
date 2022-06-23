import tkinter as tk

def operacao(op, num, v_texto, botao):
    v_texto.set(f'{num.get()} {op}')
    num.delete(0, len(f'{num}'))
    botao['relief'] = tk.SUNKEN

def igualdade(v_texto, num, botoes):
    t = f'{v_texto.get()}'
    t = t.split()
    
    for b in botoes:
        b['relief'] = tk.RAISED

    if t[1] == '+':
        r = int(t[0]) + int(num.get())
    if t[1] == '/':
        r = int(t[0]) / int(num.get())
    if t[1] == '*':
        r = int(t[0]) * int(num.get())
        
    v_texto.set(f'{t[0]} {t[1]} {num.get()} = {r}')
    num.delete(0, len(f'{num}'))

def main():
    tela = tk.Tk()
    tela.title('Calculadora')

    v_texto = tk.StringVar(value='')
    tam = 32

    num = tk.Entry(tela, font=('Arial', tam))
    num.pack()

    soma = tk.Button(tela, text='+', font=('Arial', tam), command=lambda: operacao('+', num, v_texto, soma))
    soma.pack(side=tk.LEFT)

    div = tk.Button(tela, text='/', font=('Arial', tam), command=lambda: operacao('/', num, v_texto, div))
    div.pack(side=tk.LEFT)

    mult = tk.Button(tela, text='*', font=('Arial', tam), command=lambda: operacao('*', num, v_texto, mult))
    mult.pack(side=tk.LEFT)

    botoes = [soma, div, mult]

    igual = tk.Button(tela, text='=', font=('Arial', tam), command=lambda: igualdade(v_texto, num, botoes))
    igual.pack(side=tk.LEFT)

    texto = tk.Label(tela, textvariable=v_texto, font=('Arial', tam))
    texto.pack(side=tk.BOTTOM)

    tela.mainloop()

if __name__ == '__main__':
    main()