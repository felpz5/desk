# Questão 7:
# Em uma aplicação de calculadora, você precisa adicionar dois botões,
# um chamado "Somar" e outro chamado "Subtrair".

import tkinter as tk

janela = tk.Tk()

botao_somar = tk.Button(janela, text="Somar")
botao_somar.pack(side="left", padx=10)

botao_subtrair = tk.Button(janela, text="Subtrair")
botao_subtrair.pack(side="left", padx=10)

janela.mainloop()
