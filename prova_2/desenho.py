import tkinter as tk

class QuadroDeDesenho(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('POO - Prova2')
        self.canvas = tk.Canvas(self, height=300, width=300)
        self.canvas.pack()

    def adiciona_forma(self, forma):
        if forma.__class__.__name__ == 'Circulo':
            self.canvas.create_oval(forma.desenha(), fill=forma.cor, outline='white')
        else:
            self.canvas.create_polygon(forma.desenha(), fill=forma.cor, outline='white')

    def desenha(self):
        self.mainloop()