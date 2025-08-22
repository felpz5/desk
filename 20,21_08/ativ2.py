"""
Atividade 2 – Resultado escolar

Situação:
Uma escola quer automatizar o sistema de boletins. O programa deve dizer ao aluno se
ele está aprovado, em recuperação ou reprovado, com base na nota final.

Tarefa do aluno:
- Criar um programa com Tkinter que peça a nota final do aluno (0 a 10).
- Ao clicar no botão:
    • Se a nota for >= 7 → mostre 'Aprovado'.
    • Se for entre 5 e 6.9 → mostre 'Recuperação'.
    • Se for < 5 → mostre 'Reprovado'.
"""

import tkinter as tk
from tkinter import messagebox

def verificar_nota():
    try:
        nota = float(entrada.get())
        if nota >= 7:
            messagebox.showinfo("Resultado", "Aprovado")
        elif 5 <= nota < 7:
            messagebox.showinfo("Resultado", "Recuperação")
        else:
            messagebox.showinfo("Resultado", "Reprovado")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido.")

janela = tk.Tk()
janela.title("Resultado Escolar")
janela.geometry("400x250")

tk.Label(janela, text="Digite a nota final (0 a 10):").pack(pady=5)
entrada = tk.Entry(janela)
entrada.pack(pady=5)

tk.Button(janela, text="Verificar", command=verificar_nota).pack(pady=10)

janela.mainloop()
