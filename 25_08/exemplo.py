import customtkinter as ctk 
from tkinter import messagebox

# Configura o tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela principal
root = ctk.CTk()
root.title('Tela de Login')
root.geometry('1500x950')

# Rótulo e campo do usuário
label_usuario = ctk.CTkLabel(root, text='Usuário:')
label_usuario.pack(pady=(20, 5))
entry_usuario = ctk.CTkEntry(root, placeholder_text='Digite seu usuário')
entry_usuario.pack(pady=5)

# Rótulo e campo da senha
label_senha = ctk.CTkLabel(root, text='Senha:')
label_senha.pack(pady=(20, 5))
entry_senha = ctk.CTkEntry(root, placeholder_text='Digite sua senha')  
entry_senha.pack(pady=5)


usuarios_salvos = []


def salvar_usuario():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario and senha:
        usuarios_salvos.append((usuario, senha))
        messagebox.showinfo("Salvo", f"Usuário '{usuario}' salvo com sucesso!")
        entry_usuario.delete(0, 'end')
        entry_senha.delete(0, 'end')
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos.")


def cancelar():
    root.destroy()

# Frame para botões
frame_botoes = ctk.CTkFrame(root)
frame_botoes.pack(pady=20)

# Botões
btn_entrar = ctk.CTkButton(frame_botoes, text='Entrar', command=salvar_usuario)
btn_entrar.grid(row=0, column=0, padx=10, pady=10)

btn_cancelar = ctk.CTkButton(frame_botoes, text='Cancelar', fg_color='red', hover_color="#a83232", command=cancelar)
btn_cancelar.grid(row=0, column=1, padx=10, pady=10)
 
root.mainloop()
import customtkinter as ctk
from tkinter import messagebox  # Importando messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela principal
janela = ctk.CTk()
janela.title("GamePoint")
janela.geometry("500x500")

# Funções para trocar telas
def mostrar_cadastro():
    frame_login.pack_forget()
    frame_cadastro.pack(pady=50)

def mostrar_login():
    frame_cadastro.pack_forget()
    frame_login.pack(pady=50)

def entrar():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    if usuario == "" or senha == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
    else:
        messagebox.showinfo("Login", f"Bem-vindo, {usuario}!")
        frame_login.pack_forget()
        frame_gamepoint.pack(pady=20)

def cadastrar():
    novo_usuario = entry_novo_usuario.get()
    nova_senha = entry_nova_senha.get()
    if novo_usuario == "" or nova_senha == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
    else:
        messagebox.showinfo("Cadastro", f"Usuário {novo_usuario} cadastrado com sucesso!")
        mostrar_login()

def comprar(jogo):
    messagebox.showinfo("Compra", f"Você comprou o jogo: {jogo}")

# ----- TELA LOGIN -----
frame_login = ctk.CTkFrame(janela)
frame_login.pack(pady=50)

label_login = ctk.CTkLabel(frame_login, text="Login")
label_login.pack(pady=10)

entry_usuario = ctk.CTkEntry(frame_login, placeholder_text="Usuário")
entry_usuario.pack(pady=5)

entry_senha = ctk.CTkEntry(frame_login, placeholder_text="Senha", show="*")
entry_senha.pack(pady=5)

btn_entrar = ctk.CTkButton(frame_login, text="Entrar", command=entrar)
btn_entrar.pack(pady=10)

btn_cadastrar = ctk.CTkButton(frame_login, text="Cadastrar", command=mostrar_cadastro)
btn_cadastrar.pack(pady=5)

# ----- TELA CADASTRO -----
frame_cadastro = ctk.CTkFrame(janela)

label_cadastro = ctk.CTkLabel(frame_cadastro, text="Cadastrar Novo Usuário")
label_cadastro.pack(pady=10)

entry_novo_usuario = ctk.CTkEntry(frame_cadastro, placeholder_text="Novo usuário")
entry_novo_usuario.pack(pady=5)

entry_nova_senha = ctk.CTkEntry(frame_cadastro, placeholder_text="Nova senha", show="*")
entry_nova_senha.pack(pady=5)

btn_confirmar = ctk.CTkButton(frame_cadastro, text="Cadastrar", command=cadastrar)
btn_confirmar.pack(pady=10)

btn_voltar = ctk.CTkButton(frame_cadastro, text="Voltar", command=mostrar_login)
btn_voltar.pack(pady=5)

# ----- TELA GAMEPOINT -----
frame_gamepoint = ctk.CTkFrame(janela)

label_gp = ctk.CTkLabel(frame_gamepoint, text="Bem-vindo ao GamePoint!")
label_gp.pack(pady=10)

# Lista de jogos
jogos = ["The Legend of Python", "CodeCraft", "Algo Adventure"]

for jogo in jogos:
    jogo_frame = ctk.CTkFrame(frame_gamepoint)
    jogo_frame.pack(pady=5, padx=10, fill="x")
    
    lbl = ctk.CTkLabel(jogo_frame, text=jogo)
    lbl.pack(side="left", padx=10)
    
    btn = ctk.CTkButton(jogo_frame, text="Comprar", command=lambda j=jogo: comprar(j))
    btn.pack(side="right", padx=10)

janela.mainloop()
