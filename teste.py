import tkinter as tk 

def abrir_segunda_tela():
    segunda_tela = tk.Toplevel()
    segunda_tela.title("segunda tela")
    segunda_tela.geometry("300x200")

    label2 = tk.Label(segunda_tela, text=" Você está aqui!", font= ("Arial", 13))
    label2.pack(pady=20)
    
    btn_voltar = tk.Button(segunda_tela, text="Fechar", command=segunda_tela.destroy)
    btn_voltar.pack()


    #tela principal
    root = tk.Tk()
    root.title("Tela Principal")
    root.geometry("300x200")

    label = tk.Label(root,text="Bem-Vindo!", font=("Arial",12) )
    label.pack(pady=20)

    botao_ir = tk.Button(root, text="Ir para segunda tela", command=abrir_segunda_tela)
    botao_ir.pack()

    root.mainloop()
    
    
    
