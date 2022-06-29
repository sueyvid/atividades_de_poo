import tkinter as tk

class Interface:
    def __init__(self, master):
        self.master = master
        c = Calculadora(master)

class Calculadora(Interface):
    def __init__(self, master):
        self.master = master
        self.objetos = list()
        self.cria_visor()
        self.cria_botoes()
        self.imprime_lista_objetos()
        self.config_objetos()
    
    def cria_visor(self):
        self.visor = tk.Entry(self.master, width=12)
        self.visor.grid(row=0, column=0, columnspan=3, sticky='NSWE')
        self.objetos.append(self.visor)

        self.texto_conta = tk.StringVar(value='')
        self.conta = tk.Label(self.master, textvariable=self.texto_conta, font=('', 13))
        self.conta.grid(row=0, column=0, columnspan=2, sticky='NW')

    def cria_botoes(self):
        self.num = dict()
        k = 1
        for i in range(3):
            for j in range(3):
                self.num[f'{k}'] = tk.Button(self.master, text=f'{k}')
                self.num[f'{k}'].grid(row=3-i, column=j, sticky='WE')
                self.objetos.append(self.num[f'{k}'])
                print(k)
                k += 1
        
        self.num['0'] = tk.Button(self.master, text='0')
        self.num['0'].grid(row=4, column=0, columnspan=3, sticky='WE')
        self.objetos.append(self.num['0'])

        self.botoes = dict()
        self.botoes = self.num.copy()

        self.botoes['+'] = tk.Button(self.master, text='+')
        self.botoes['+'].grid(row=1, column=3, sticky='WE')
        self.objetos.append(self.botoes['+'])

        self.botoes['/'] = tk.Button(self.master, text='/')
        self.botoes['/'].grid(row=2, column=3, sticky='WE')
        self.objetos.append(self.botoes['/'])

        self.botoes['*'] = tk.Button(self.master, text='*')
        self.botoes['*'].grid(row=3, column=3, sticky='WE')
        self.objetos.append(self.botoes['*'])

        self.botoes['='] = tk.Button(self.master, text='=')
        self.botoes['='].grid(row=4, column=3, sticky='WE')
        self.objetos.append(self.botoes['='])

        self.botoes['<'] = tk.Button(self.master, text='<')
        self.botoes['<'].grid(row=0, column=3)
        self.objetos.append(self.botoes['<'])

        self.num['1']['command'] = lambda: self.add_num('1')
        self.num['2']['command'] = lambda: self.add_num('2')
        self.num['3']['command'] = lambda: self.add_num('3')
        self.num['4']['command'] = lambda: self.add_num('4')
        self.num['5']['command'] = lambda: self.add_num('5')
        self.num['6']['command'] = lambda: self.add_num('6')
        self.num['7']['command'] = lambda: self.add_num('7')
        self.num['8']['command'] = lambda: self.add_num('8')
        self.num['9']['command'] = lambda: self.add_num('9')
        self.num['0']['command'] = lambda: self.add_num('0')
        self.botoes['<']['command'] = lambda: self.remove_num()
        self.botoes['+']['command'] = lambda: self.operacao('+')
        self.botoes['/']['command'] = lambda: self.operacao('/')
        self.botoes['*']['command'] = lambda: self.operacao('*')
        self.botoes['=']['command'] = lambda: self.resultado()

    def add_num(self, num):
        self.visor.insert(len(self.visor.get()), num)
    
    def remove_num(self):
        self.visor.delete(len(self.visor.get())-1)
        if self._op == '':
            self.texto_conta.set('')
        if self.botoes['<']['text'] == 'C':
            self.botoes['<']['text'] = '<'
            self.visor.delete(0, len(self.visor.get()))
    
    def operacao(self, op):
        if self.botoes['<']['text'] == 'C':
            self.botoes['<']['text'] = '<'
        self._num = self.visor.get()
        self._op = op
        self.visor.delete(0, len(self.visor.get()))
        self.botoes[op]['relief'] = tk.SUNKEN
        self.texto_conta.set(f'{self._num} {self._op}')
    
    def resultado(self):
        self._num2 = self.visor.get()
        if self._op == '+':
            self._resultado = float(self._num) + float(self.visor.get())
        if self._op == '/':
            self._resultado = float(self._num) / float(self.visor.get())
        if self._op == '*':
            self._resultado = float(self._num) * float(self.visor.get())
        self.botoes['<']['text'] = 'C'
        self.visor.delete(0, len(self.visor.get()))
        self.visor.insert(0, str(self._resultado))
        self.texto_conta.set(f'{self._num} {self._op} {self._num2} = ')
        self._op = ''
        for b in self.botoes.values():
            b['relief'] = tk.RAISED

    def imprime_lista_objetos(self):
        # print(self.objetos)
        print(self.botoes)

    def config_objetos(self):
        for obj in self.objetos:
            obj['font'] = ('', 18)
        for obj in self.botoes.values():
            obj['width'] = 4
            obj['height'] = 2
        # for i in range(9):
        #     self.num[f'{i}']['command'] = lambda: print(i, self.num[f'{i}'])
        # for i in range(9):
        #     print(i)
        #     i['command'] = lambda: print(int(f'{i}'))
            # print(self.num[f'{i}']['text'])
            # self.num[f'{i}']['command'] = lambda: print(self.num[f'{i}']['text'])
        #     print(self.num[f'{i}'])

def main():
    tela = tk.Tk()
    tela.title('Calculadora')
    i = Interface(tela)
    tela.mainloop()

if __name__ == '__main__':
    main()