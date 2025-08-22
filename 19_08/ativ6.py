# Questão 6:
# Você está criando um formulário simples para coletar o nome do usuário.
# Faça um programa com uma janela contendo um rótulo (Label) "Digite seu nome:" 
# e uma caixa de texto (Entry) logo abaixo.

import tkinter as tk

janela = tk.Tk()

tk.Label(janela, text="Digite seu nome:").pack()
entrada = tk.Entry(janela)
entrada.pack()

janela.mainloop()
