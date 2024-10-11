import sqlite3

#crinado uma conexão com um banco de dados
conn = sqlite3.connect('mydatabase.db')

#deletar dados da tabela
conn.execute("DELETE from stocks WHERE symbol = 'IBM'")

#Salvando as alterações
conn.commit()

#Fecha a conexão com o banco
conn.close()