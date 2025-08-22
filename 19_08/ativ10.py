# Questão 10:
# Você quer fazer um botão que, ao ser clicado, fecha a janela principal.
# Crie o programa com um botão chamado "Sair", que encerra a aplicação.

import tkinter as tk

janela = tk.Tk()
janela.geometry("400x250")

botao_sair = tk.Button(janela, text="Sair", command=janela.destroy)
botao_sair.pack(pady=15)

janela.mainloop()
