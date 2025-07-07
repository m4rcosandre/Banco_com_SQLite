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
criuar_tabela1 = """CREATE TABLE CONTATOS(
                ID_CONTATO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                NOME_CONTATO VARCHAR(30) NOT NULL,
                TELEFONE_CONTATO VARCHAR (11) NOT NULL,
                EMAIL_CONTATO VARCHAR(30) NOT NULL
);"""

##########inserir valores na tabela 
inserir_valor = """INSERT INTO CONTATOS
                      (NOME_CONTATO,TELEFONE_CONTATO,EMAIL_CONTATO)
                  VALUES('Marcos André Oliveira dos Santos','(82)99876-5432-','m4rcos.oliveira19@gmail.com')"""
def criar_tabela(conexao,sql):
  try:
    cursor=conexao.cursor()
    cursor.execute(sql)
    print('tabela criada')
  except Error as ex:
    print(ex)

def inserir(conexao,sql):
  try:
    cursor = conexao.cursor()
    cursor.execute(sql)
    cursor.commit()
    print('Inserido com sucesso')
  except Error as ex:
    print(ex)

##########CHAMADAS
#criar_tabela(vcon,criuar_tabela1)
inserir(vcon,inserir_valor)


vcon.close()