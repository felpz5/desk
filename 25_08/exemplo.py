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
