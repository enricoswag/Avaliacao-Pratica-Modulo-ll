"""
Avaliação – Python + SQLite
Tema: CRUD em 'alunos'

O que o script deve fazer:
1) Criar 'escola.db'
2) Criar tabela 'alunos' -> Seguindo o diagrama
3) Inserir registros na tabela alunos
4) Listar todos
5) Buscar por id
6) Atualizar registros
7) Deletar registros
0
"""
import sqlite3
# Passo 1 - Conectar/criar o banco de dados
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Passo 2 - Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT
               )
""")

print("Tabela criada com sucesso!\n")

# Passo 3 - Inserir dados
cursor.execute("INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)",
               ("Shisui",18, "shisui@gmail.com"))
cursor.execute("INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)",
               ("Nemos",17, "nemos@gmail.com"))
cursor.execute("INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)",
               ("Jovem",15, "jovem@gmail.com"))
cursor.execute("INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)",
               ("Enrico",67, "enrico@gmail.com"))
conn.commit()

print("Dados inseridos!\n")

# Passo 4 - Listar todos
cursor.execute("SELECT * FROM alunos")
for linha in cursor.fetchall():
    print(linha)
print()
# Passo 5
cursor.execute('UPDATE alunos SET email = ? WHERE nome = ?',
               ('enrico.dev@gmail.com', 'Enrico'))
conn.commit()
print('Após atualização do email do José:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)

print()

#passo 6
cursor.execute('DELETE FROM alunos WHERE nome = ?', ('Gustavo',))
conn.commit()
print('Após deletar do email do Gustavo:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

# Encerrar conexão

conn.close()
