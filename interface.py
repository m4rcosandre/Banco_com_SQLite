from tkinter import *
import Agenda


janela =Tk()
janela.title("Agenda de Contatos")
janela.geometry("400x300") 


nome = Label(janela, text="Nome Completo:")
nome.place(x=20, y=20)

n1 = Entry(janela)
n1.place(x=20, y=50, width=200, height=20)


idade = Label(janela, text="idade:")
idade.place(x=20, y=80)

i1 = Entry(janela)
i1.place(x=20, y=110, width=200, height=20)

email = Label(janela, text="E-mail:")
email.place(x=20, y=140)

e1 = Entry(janela)
e1.place(x=20, y=170, width=200, height=20)


cep = Label(janela, text="CEP:")
cep.place(x=20, y=200)

c1 = Entry(janela)
c1.place(x=20, y=230, width=200, height=20) 


















janela.mainloop()