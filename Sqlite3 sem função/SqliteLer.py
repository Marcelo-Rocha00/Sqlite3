import sqlite3

#criando uma conexão com um banco de dados
conn = sqlite3.connect('mydatabase.db')

#selecionando todos os dados da tabela
curso = conn.execute("SELECT * from stocks")

#iterar sobre os dados e exibi-los
for row in curso:
    print(row)


#Salvando as alterações
conn.commit()

#Fecha a conexão com o banco
conn.close()