"""
Atividade 1 – Controle de acesso por idade

Situação:
Uma empresa precisa de um programa para verificar se a pessoa tem idade suficiente
para entrar em um evento que exige ser maior de idade.

Tarefa do aluno:
- Criar um programa em Python com Tkinter que tenha uma janela com um campo para o usuário digitar sua idade.
- Ao clicar em um botão, verificar:
    • Se a idade for menor que 18 anos → exiba 'Você é menor de idade.'
    • Se for 18 ou mais → exiba 'Você é maior de idade.'
"""

import tkinter as tk
from tkinter import messagebox

def verificar_idade():
    try:
        idade = int(entrada.get())
        if idade < 18:
            messagebox.showinfo("Resultado", "Você é menor de idade.")
        else:
            messagebox.showinfo("Resultado", "Você é maior de idade.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido.")

janela = tk.Tk()
janela.title("Controle de Acesso por Idade")
janela.geometry("400x250")

tk.Label(janela, text="Digite sua idade:").pack(pady=5)
entrada = tk.Entry(janela)
entrada.pack(pady=5)

tk.Button(janela, text="Verificar", command=verificar_idade).pack(pady=10)

janela.mainloop()
