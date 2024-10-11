import sqlite3

#criando uma conexão com um banco de dados
conn = sqlite3.connect('mydatabase.db')

coluna = input("insira qual coluna deseja alterar o valor")
tabela = input("insira qual tabela deseja altera")
valor = input("insira o valor que deseja alterar")

#atualizar dados na tabela
conn.execute(f"UPDATE stocks SET price = {valor} WHERE {coluna} = {tabela}")

#Salvando as alterações
conn.commit()

#Fecha a conexão com o banco
conn.close()