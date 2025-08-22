# Questão 8:
# Imagine que você está desenvolvendo um programa de aviso.
# Crie uma janela com um rótulo (Label) escrito "Atenção!" em fonte grande e em vermelho.

import tkinter as tk

janela = tk.Tk()

aviso = tk.Label(janela, text="Atenção!", font=("Arial", 24), fg="red")
aviso.pack()

janela.mainloop()
