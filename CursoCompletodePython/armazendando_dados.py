import sqlite3

conexao = sqlite3.connect('aula44.db')
c = conexao.cursor()

c.execute("CREATE TABLE IF NOT EXISTS usuario(id integer, nome text)")

# c.execute("INSERT INTO usuario VALUES(1, 'Marcelo')")
# c.execute("INSERT INTO usuario VALUES(2, 'Jafferson')")
# c.execute("INSERT INTO usuario VALUES(3, 'Rodrigo')")

# conexao.commit()

requisicao = 'SELECT * FROM usuario WHERE nome = ?'

for linha in c.execute(requisicao, ('Marcelo',)): # exemplo do que esta sendo pesquisado no banco de dados
    print(linha)
