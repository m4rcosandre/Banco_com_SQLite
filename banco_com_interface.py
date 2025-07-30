import sqlite3
from sqlite3 import Error
from tkinter import *

def conexao():
  caminho = 'C:\\Users\\kkded\\OneDrive\\Área de Trabalho\\Projetos P\\Banco_com_SQLite\\banco_com_interface'

  try:
    con = sqlite3.connect(caminho)
    print('Banco conectado com sucesso')
  except Error as e:
    print(e)
  return con

vcon = conexao()

def inserir_tabela(conexao,nome,idade,serie):
  sql = """INSERT INTO ALUNOS
            (NOME,IDADE,SERIE) 
            VALUES(?,?,?)"""
  dados = (nome,idade,serie)

  try:
    cursor =conexao.cursor() 
    cursor.execute(sql,dados)
    conexao.commit()
    return 'comitado com sucesso'
  except Error as e:
    return f'{e}'


def deletar(conexao,id):
  
  sql = """DELETE FROM ALUNOS WHERE ID = ?"""
  
  try:
    cursor = conexao.cursor()
    cursor.execute(sql,(id,))
    conexao.commit()
    return 'comitado com sucesso'
  except Error as e:
    return f'{e}'
  
def atualizar(conexao,id,nome,idade,serie):
  
  sql = """UPDATE ALUNOS SET NOME = ?, IDADE = ?, SERIE = ? WHERE ID = ?"""

  try:
    cursor = conexao.cursor()
    cursor.execute(sql,(nome,idade,serie,id))
    conexao.commit()
    return 'comitado com sucesso'
  except Error as e:
    return f'{e}'
  


def inserir_dados():
  n = nome1.get()
  i = idade1.get()
  s = serie1.get()
  resultado = inserir_tabela(vcon,n,i,s)
  print(resultado)

  #Deleta os dados dentro do campo para colocar novos 
  nome1.delete(0, END)
  idade1.delete(0, END)
  serie1.delete(0, END)

def deletar_dados():
    id_valor = id_entry.get()

    if id_valor.strip() == "":
        print("Digite um ID válido.")
        return

    resultado = deletar(vcon, id_valor)
    print(resultado)

    # Limpar o campo de ID após deletar
    id_entry.delete(0, END)




app = Tk()
app.title('DADOS')
app.geometry('500x700')


nome = Label(text='Nome', )
nome.place(x=20,y=30)

nome1 = Entry(app)
nome1.place(x=20,y=60, width=300)

#---------

idade = Label(text='IDADE', )
idade.place(x=20,y=90)

idade1 = Entry(app)
idade1.place(x=20,y=120, width=300)

#---------

serie = Label(text='Série', )
serie.place(x=20,y=150)

serie1 = Entry(app)
serie1.place(x=20,y=180, width=300)

botão = Button(text='INSERIR DADOS',command=inserir_dados)
botão.place(x=50, y=220, width=150,)



#Label e campo para o ID
id_label = Label(text='ID para deletar:')
id_label.place(x=20, y=260)

id_entry = Entry(app)
id_entry.place(x=20, y=290, width=300)

# Botão de deletar
botao_deletar = Button(text='DELETAR DADOS', command=deletar_dados)
botao_deletar.place(x=50, y=330, width=150)







app.mainloop()
