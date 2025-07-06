import sqlite3
from sqlite3 import Error
 #############conexão
def conexao_banco():
  caminho = 'C:\\Users\\kkded\\OneDrive\\Área de Trabalho\\Projetos P\\Banco_com_SQLite\\contatos.db'
  con = None
  try:
    con = sqlite3.connect(caminho)
  except Error as ex:
    print(ex)
  return con    

vcon = conexao_banco()
#############criar tabela
tabela1 = """CREATE TABLE CONTATOS(
                ID_CONTATO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                NOME_CONTATO VARCHAR(30) NOT NULL,
                TELEFONE_CONTATO VARCHAR (11) NOT NULL,
                EMAIL_CONTATO VARCHAR(30) NOT NULL
);"""

def criar_tabela(conexao,sql):
  try:
    c=conexao.cursor()
    c.execute(sql)
    print('tabela criada')
  except Error as ex:
    print(ex)


criar_tabela(vcon,tabela1)


vcon.close()