# Questão 9:
# Você deseja deixar a janela de um programa mais amigável.
# Crie uma janela com tamanho 400x300 e um título personalizado ("Minha Aplicação Tkinter").

import tkinter as tk

janela = tk.Tk()
janela.title("Minha Aplicação Tkinter")
janela.geometry("400x300") 

janela.mainloop()
