"""
Atividade 5 – Cardápio interativo

Situação:
Um restaurante quer um sistema simples para mostrar os preços dos produtos do cardápio.
O cliente escolhe digitando um número.

Cardápio:
1 - Pizza – R$ 30,00
2 - Hambúrguer – R$ 20,00
3 - Refrigerante – R$ 5,00

Tarefa do aluno:
- Criar um programa com Tkinter que mostre o cardápio e permita o cliente digitar uma opção (1, 2 ou 3).
- Ao clicar no botão:
    • Se o cliente digitar 1 → mostre 'Pizza – R$ 30,00'.
    • Se digitar 2 → mostre 'Hambúrguer – R$ 20,00'.
    • Se digitar 3 → mostre 'Refrigerante – R$ 5,00'.
    • Qualquer outra coisa → mostre 'Opção inválida'.
"""

import tkinter as tk
from tkinter import messagebox

def verificar_opcao():
    opcao = entrada.get()
    if opcao == "1":
        messagebox.showinfo("Resultado", "Pizza – R$ 30,00")
    elif opcao == "2":
        messagebox.showinfo("Resultado", "Hambúrguer – R$ 20,00")
    elif opcao == "3":
        messagebox.showinfo("Resultado", "Refrigerante – R$ 5,00")
    else:
        messagebox.showerror("Erro", "Opção inválida")

janela = tk.Tk()
janela.title("Cardápio Interativo")
janela.geometry("400x250")

tk.Label(janela, text="Cardápio:\n1 - Pizza – R$ 30,00\n2 - Hambúrguer – R$ 20,00\n3 - Refrigerante – R$ 5,00").pack(pady=5)

tk.Label(janela, text="Digite a opção desejada:").pack(pady=5)
entrada = tk.Entry(janela)
entrada.pack(pady=5)

tk.Button(janela, text="Verificar", command=verificar_opcao).pack(pady=10)

janela.mainloop()
