import tkinter as tk 
from tkinter import ttk, messagebox 

janela = tk.Tk()
janela.geometry("820x500")
janela.title("Cadastro de cliente")
janela.configure(bg='#e6f2ff')

# Listas globais para armazenar os dados
nomes = []
emails = []
telefones = []

def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    if nome and email and telefone:
        nomes.append(nome)
        emails.append(email)
        telefones.append(telefone)
        print("Cadastro realizado com sucesso!")
        print(f"Nome: {nome}, Email: {email}, Telefone: {telefone}")
        entry_nome.delete(0,tk.END)
        entry_email.delete(0,tk.END)
        entry_telefone.delete(0,tk.END)

    


frame_dados_clientes = tk.LabelFrame(text="Dados do cliente")
frame_dados_clientes.grid()

label_nome = tk.Label(frame_dados_clientes, text="  Nome:")
label_nome.grid(row=0, column=0, padx=5, pady=5)

entry_nome = tk.Entry(frame_dados_clientes)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_email = tk.Label(frame_dados_clientes, text="  Email:")
label_email.grid(row=1, column=0, padx=5, pady=5)

entry_email = tk.Entry(frame_dados_clientes)
entry_email.grid(row=1, column=1, padx=5, pady=5)

label_telefone = tk.Label(frame_dados_clientes, text=" Telefone:")
label_telefone.grid(row=2, column=0, padx=5, pady=5)

entry_telefone = tk.Entry(frame_dados_clientes)
entry_telefone.grid(row=2, column=1, padx=5, pady=5)

#botoe

botao_cadastrar = tk.Button(frame_dados_clientes, text="Cadastrar(Entre)",command= cadastrar,bg="#447e92", fg='white')
botao_cadastrar.grid(row=4,column=0,padx=5, pady=5)

botao_limpar = tk.Button(frame_dados_clientes, text="Limpar(F2)",bg="#447e92", fg='white')
botao_limpar.grid(row=4,column=1)

botao_exculir = tk.Button(frame_dados_clientes, text="Excluir(Delete)",bg="#447e92", fg='white')
botao_exculir.grid(row=4,column=2)

botao_Desfazer = tk.Button(frame_dados_clientes, text="Deletar Apagar",bg="#447e92", fg='white')
botao_Desfazer.grid(row=4,column=3,padx=5, pady=5)

botao_salvar = tk.Button(frame_dados_clientes, text="Salvar",bg="#447e92", fg='white')
botao_salvar.grid(row=4,column=4, padx=5, pady=5)

botao_pesquisar = tk.Button(frame_dados_clientes, text="pesquisar",bg="#447e92", fg='white')
botao_pesquisar.grid(row=0, column=3, padx=5, pady=5)

entry_pesquisar = tk.Entry(frame_dados_clientes)
entry_pesquisar.grid(row= 0,  column= 4, padx=5, pady=5)

#clientes cadastrados
frame_clientes_cadastrados = tk.LabelFrame(text="Clientes Cadastrados")
frame_clientes_cadastrados.grid(padx=10, pady=10)

tree = ttk.Treeview(frame_clientes_cadastrados, column=('Id' , 'Nome' , 'Email' , 'Telefone'), show="headings")
tree.heading ('Id',text='Id')
tree.heading ('Nome',text='Nome')
tree.heading ('Email',text='Email')
tree.heading ('Telefone',text='telefone')
tree.grid(row=0, column=0)

botao_excluir_varios = tk.Button(frame_clientes_cadastrados,\
text='Remover Selecionados',bg="#447e92", fg='white' )
botao_excluir_varios.grid(row=1, column=0, padx=10, pady=5, sticky='e')
#command=excluir_selecionados, obS: tem que fazer uma função pra esse funcionar

janela.mainloop()