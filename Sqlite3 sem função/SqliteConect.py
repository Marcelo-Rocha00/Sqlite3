import sqlite3

#criar uma conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')

#criando uma tabela
conn.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')

#salva as alterações
conn.commit()

#fecha a conexão com o banco
conn.close()