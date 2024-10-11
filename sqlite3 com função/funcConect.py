import sqlite3

conn = sqlite3.connect('mercadinho.db')

def criar_banco():
    conn.execute('''CREATE TABLE estoque (data text, produto text, qty_compra real, preco_venda real)''')
    conn.commit()


def inserir_valores():
    data = input("Data da compra: ")
    produto = input("Nome do produto: ")
    qty_compra = float(input("quantidade de produtos: "))
    preco_venda = float(input("Digite o valor da compra: "))
    
    conn.execute(f"INSERT INTO estoque VALUES ('{data}', '{produto}',{qty_compra},{preco_venda})")
    conn.commit()
inserir_valores()
    
def ler_dados():
    cursor = conn.execute("SELECT * FROM estoque")
    
    for row in cursor:
        print(row)
ler_dados()

def update():
    produto = input("insira qual coluna deseja alterar o valor")
    tabela = input("insira qual tabela deseja altera")
    preco_venda = input("insira o valor que deseja alterar")
    
    conn.execute(f"UPDATE estoque SET preco_venda = {preco_venda} WHERE {produto} = {tabela}")
update()

        

conn.close()
    