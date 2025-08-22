# Questão 4:
# Você adicionou um rótulo (Label) e um botão, mas eles não aparecem corretamente organizados na tela.
# Mostre como usar o método correto (pack) para posicionar os widgets dentro da janela principal.

import tkinter as tk

janela = tk.Tk()

rotulo = tk.Label(janela, text="Sou um rótulo")
rotulo.pack()

botao = tk.Button(janela, text="Clique aqui")
botao.pack()

janela.mainloop()
