import os
import sqlite3
from sqlite3 import Error

########## CONEXÃO

def conexao():
  caminho = 'C:\\Users\\kkded\\OneDrive\\Área de Trabalho\\Projetos P\\Banco_com_SQLite\\AGENDA.db'
  con = None
  try:
    con = sqlite3.connect(caminho)
    print('Banco criado com sucesso!')
  except Error as ex:
    print(f'Erro ao criar o banco:{ex}')
  return con

vcon = conexao()

def menuprincipal():
  os.system("cls")
  print("1 - Inserir registro ")
  print("2 - Deletar registro ")
  print("3 - Atualizar registro ")
  print("4 - Consultar registro por ID")
  print("5 - Consultar registro por Nome ")
  print("6 - Sair ")

def inserir(conexao):
  os.system('cls')
  nome = input('Nome completo: ')
  numero_contato = input('Numero de contato: ')
  cep = input('CEP: ')
  email = input("Digite seu E-mail: ")
  sql = """INSERT INTO AGENDA
          (NOME_COMPLETO,NUMERO_CONTATO,CEP,EMAIL)
          VALUES(?,?,?,?)"""
  dados = (nome,numero_contato,cep, email)
  try:
    cursor = conexao.cursor()
    cursor.execute(sql,dados)
    conexao.commit()
    print('Dados inseridos com sucesso!')
  except Error as ex:
    print(ex)
  
def deletar(conexao):
  os.system('cls')
  n1 = int(input('Qual o ID dos dados que deseja deletar: '))
  sql = """DELETE FROM AGENDA WHERE ID= ?"""
  dados = (n1,)
  try:
    cursor = conexao.cursor()
    cursor.execute(sql,dados)
    conexao.commit()
    print('dado deletado com sucesso')
  except Error as ex:
    print(ex)
def atualizar():
  os.system('cls')
  
def consultar_id():
  print()

def consulta_nome():
  print()

  
opcao = 0
while opcao != 6:
  menuprincipal()
  opcao = int(input('Digite uma opção: '))

  if opcao == 1:
    inserir(vcon)
  elif opcao ==2:
    deletar(vcon) 
  elif opcao == 3:
    atualizar(vcon)
  elif opcao == 4:
    consultar_id(vcon)
  elif opcao == 5:
    consulta_nome(vcon)
  elif opcao == 6:
    os.system('cls')
    print("Obrigado e volte sempre!") 
    vcon.close()
  else:
    os.system("cls")
    print('Opção inválida')
    os.system('pause')


os.system('pause')
    

print(menuprincipal)
