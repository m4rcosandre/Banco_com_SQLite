import sqlite3
from sqlite3 import Error
 ##########conexão
def conexao_banco():
  caminho = 'C:\\Users\\kkded\\OneDrive\\Área de Trabalho\\Projetos P\\Banco_com_SQLite\\contatos.db'
  con = None
  try:
    con = sqlite3.connect(caminho)
  except Error as ex:
    print(ex)
  return con    

vcon = conexao_banco()

##########criar tabela
criar_tabela1 = """CREATE TABLE CONTATOS(
                ID_CONTATO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                NOME_CONTATO VARCHAR(30) NOT NULL,
                TELEFONE_CONTATO VARCHAR (11) NOT NULL,
                EMAIL_CONTATO VARCHAR(30) NOT NULL
);"""

##########inserir valores na tabela 
#nome = input('Digite o seu nome: ')
#tel = input('Digite o seu contato: ')
#email = input('Digite o seu e-mail: ')
#inserir_valor = """INSERT INTO CONTATOS
#                      (NOME_CONTATO,TELEFONE_CONTATO,EMAIL_CONTATO)
#                  VALUES(?,?,?)"""
#dados = (nome,tel, email)

##########Deletar valores da tabela
deletar_valor = """DELETE FROM CONTATOS WHERE ID_CONTATO=9"""

##########Atualizar valor
atualizar_tabela = """UPDATE CONTATOS SET NOME_CONTATO='SANDRO' WHERE ID_CONTATO = 10"""

##########Consultar tabela
consultar_tabela = """SELECT * FROM CONTATOS """

def criar_tabela(conexao,sql):
  try:
    cursor=conexao.cursor() 
    cursor.execute(sql)
    print('tabela criada')
  except Error as ex:
    print(ex)

def inserir(conexao,sql,dados):
  try:
    cursor = conexao.cursor()
    cursor.execute(sql,dados)
    conexao.commit()
    print('Inserido com sucesso')
  except Error as ex:
    print(ex)

def deletar(conexao,sql):
  try:
    cursor = conexao.cursor()
    cursor.execute(sql)
    conexao.commit()
    print('Itens deletados com sucesso')
  except Error as ex:
    print(ex)

def atualizar(conexao,sql):
  try:
    cursor = conexao.cursor()
    cursor.execute(sql)
    conexao.commit()
    print('Valor atualizado com sucesso')
  except Error as ex:
    print(ex)

def consultar(conexao,sql):
  cursor = conexao.cursor()
  cursor.execute(sql)
  resultado = cursor.fetchall()
  return resultado
  


##########CHAMADAS
#criar_tabela(vcon,criar_tabela1)
#inserir(vcon,inserir_valor,dados)
#deletar(vcon,deletar_valor)
#atualizar(vcon,atualizar_tabela)
res = consultar(vcon,consultar_tabela)
for r in res:
  print(r)



vcon.close()