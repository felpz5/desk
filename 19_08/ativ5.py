# Questão 5:
# Em uma aplicação, ao clicar em um botão, você quer abrir uma nova janela chamada "Segunda Tela".

import tkinter as tk

def abrir_segunda_tela():
    nova_janela = tk.Toplevel()
    nova_janela.title("Segunda Tela")
    tk.Label(nova_janela, text="Bem-vindo à segunda tela!").pack()

janela = tk.Tk()
botao = tk.Button(janela, text="Abrir segunda tela", command=abrir_segunda_tela)
botao.pack()

janela.mainloop()
