from tkinter import *
from tkinder import messagebox
janela = Tk()
janela.title("Algoritmos")
janela.geometry("400x400")


rotulo = Label(janela, text="hello GUI", font=("Arial bold", 20))
rotulo.place(x=200, y=100, anchor="center")

entrada = Entry(janela, width=14, font=("Arial bold", 14))
entrada.place(x=200, y=300, anchor="center")



def show():
    res = messagebox.showinfo("aviso", "o botao foi clicado")
    print(res)


btn1 = Button(janela, text="botao1", command=show)
btn1.place(relx = 0.5 , rely = 0.5, anchor = "center")

btn2 = Button(janela, text="botao2", command=show)
btn2.place(relx = 0.5 , rely = 0.6, anchor = "center")



janela.mainloop()

