"""
Atividade 4 – Sistema de senha

Situação:
Um sistema de segurança precisa verificar se a senha digitada pelo usuário está correta.
A senha correta é '1234'.

Tarefa do aluno:
- Criar um programa com Tkinter que tenha um campo para o usuário digitar a senha.
- Ao clicar no botão:
    • Se a senha for '1234' → mostre 'Acesso permitido'.
    • Caso contrário → mostre 'Acesso negado'.
"""

import tkinter as tk
from tkinter import messagebox

def verificar_senha():
    senha = entrada.get()
    if senha == "1234":
        messagebox.showinfo("Resultado", "Acesso permitido")
    else:
        messagebox.showerror("Resultado", "Acesso negado")

janela = tk.Tk()
janela.title("Sistema de Senha")
janela.geometry("400x250")

tk.Label(janela, text="Digite a senha:").pack(pady=5)
entrada = tk.Entry(janela, show="*")
entrada.pack(pady=5)

tk.Button(janela, text="Entrar", command=verificar_senha).pack(pady=10)

janela.mainloop()
