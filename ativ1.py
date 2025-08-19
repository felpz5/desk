import tkinter as tk 
#janela principal
janela = tk.Tk()
janela.title("Janela principal")
janela.geometry("300x200")

#rotulo
rotulo = tk.Label(janela, text="Olá!", font=("Arial", 15))
rotulo.pack()

#butao
butao = tk.Button(janela, text="Clique Aqui!")
butao.pack()

#segunda tela
def abrir_segunda_tela():
    segunda = tk.Toplevel(janela)
    segunda.title("Segunda Janela ")
    segunda.geometry("300x200")
    tk.Label(segunda, text=" Você abril a segunda tela").pack()

#butao para abrir segunda tela
butao2 = tk.Button(janela, text="Abrir segunda tela", command= abrir_segunda_tela)
butao2.pack()


janela.mainloop()