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
#---------------------------------------------------------
def menuprincipal():
  os.system("cls")
  print("1 - Inserir registro ")
  print("2 - Deletar registro ")
  print("3 - Atualizar registro ")
  print("4 - Consultar registro ")
  print("5 - Sair ")
#---------------------------------------------------------
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
#---------------------------------------------------------  
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
#---------------------------------------------------------
def atualizar(conexao):
  os.system('cls')
  id_registro = input('Qual o ID que deseja atualizar?:')

  print("\n--- Campos para Atualizar ---")
  print("1- Nome completo")
  print("2- Número contato")
  print("3- CEP")
  print("4- E-mail")
  opcao_campo = int(input("Escolha o número de campo que deseja atualizar: "))

  coluna = "" 
  novo_valor = ""
  sql = ""
  
  if opcao_campo == 1:
    coluna = 'NOME_COMPLETO'
    novo_valor = input('Qual é o novo nome?: ')
  elif opcao_campo == 2:
    coluna = 'NUMERO_CONTATO'
    novo_valor = input('Qual é o novo CONTATO: ')
  elif opcao_campo == 3:
    coluna = 'CEP'
    novo_valor = input('Qual é o novo CEP: ')
  elif opcao_campo == 4:
    coluna = 'EMAIL'
    novo_valor = input('Qual é o novo E-mail: ')
  else:
    print('Infelizmente não temos essa opção, tente novamente!')
    return
  
  sql = f"UPDATE AGENDA SET {coluna} = ? WHERE ID = ?"
  dados = (novo_valor,id_registro)

  try:
    cursor = conexao.cursor()
    cursor.execute(sql,dados)
    conexao.commit()
  except Error as ex:
    print(ex)
#---------------------------------------------------------
def consultar(conexao):
  os.system('cls')
  sql = """SELECT * FROM AGENDA """
  try:
    cursor = conexao.cursor()
    cursor.execute(sql)
    registros = cursor.fetchall()
  
    if len(registros) == 0:
      print('Nenhum registro encontrado')
    else:
      print('Registros encontrados')
      for registro in registros:
        print(f'ID: {registro[0]} \nNome: {registro[1]} \nContato{registro[2]} \nCEP: {registro[3]} \nEmail: {registro[4]}')
        print('--------------------------------------------------')
  except Error as ex:
    print(ex)
  input('Precione "ENTER" para sair!')
#---------------------------------------------------------


  
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
    consultar(vcon)
  elif opcao == 5:
    os.system('cls')
    print("Obrigado e volte sempre!") 
    vcon.close()
  else:
    os.system("cls")
    print('Opção inválida')
    os.system('pause')


os.system('pause')
    

print(menuprincipal)
