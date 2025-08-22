# Questão 3:
# Você quer adicionar um botão chamado "Clique aqui" na tela principal do programa.

import tkinter as tk

janela = tk.Tk()

botao = tk.Button(janela, text="Clique aqui")
botao.pack()  

janela.mainloop()
