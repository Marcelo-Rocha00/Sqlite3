import sqlite3

#criando uma conexão com um banco de dados
conn = sqlite3.connect('mydatabase.db')

#inserindo dados na tabela
conn.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY','RHAT',100,35.14)")
conn.execute("INSERT INTO stocks VALUES ('2006-03-28','SELL', 'IBM',1000,45.00) ")
conn.execute("INSERT INTO stocks VALUES ('2006-04-06','SELL','IBM',500,53.00) ")

#Salvando as alterações
conn.commit()

#Fecha a conexão com o banco
conn.close()