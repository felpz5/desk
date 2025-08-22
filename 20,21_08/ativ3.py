"""
Atividade 3 – Identificador de números

Situação:
Um professor de matemática quer um programa que diga se um número é positivo,
negativo ou igual a zero.

Tarefa do aluno:
- Criar um programa em Tkinter que permita ao usuário digitar um número.
- Ao clicar no botão:
    • Se o número > 0 → mostre 'Número positivo'.
    • Se < 0 → mostre 'Número negativo'.
    • Se = 0 → mostre 'Número igual a zero'.
"""

import tkinter as tk
from tkinter import messagebox

def verificar_numero():
    try:
        num = float(entrada.get())
        if num > 0:
            messagebox.showinfo("Resultado", "Número positivo")
        elif num < 0:
            messagebox.showinfo("Resultado", "Número negativo")
        else:
            messagebox.showinfo("Resultado", "Número igual a zero")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido.")

janela = tk.Tk()
janela.title("Identificador de Números")
janela.geometry("400x250")

tk.Label(janela, text="Digite um número:").pack(pady=5)
entrada = tk.Entry(janela)
entrada.pack(pady=5)

tk.Button(janela, text="Verificar", command=verificar_numero).pack(pady=10)

janela.mainloop()
