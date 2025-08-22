# Questão 2:
# Um colega criou a janela principal do Tkinter, mas quando executa o programa,
# ela fecha imediatamente. Escreva a linha de código que faz a janela permanecer aberta.

import tkinter as tk

janela = tk.Tk()
janela.geometry("400x250")
janela.mainloop()  
