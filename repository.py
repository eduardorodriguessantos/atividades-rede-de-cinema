from connection import Connection

class FilmeRepository:
    def __init__(self):
        self.init_db()

    def init_db(self):
        with Connection.get_connection() as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS filmes 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             titulo TEXT, duracao INTEGER)''')

    def salvar(self, filme):
        with Connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO filmes (titulo, duracao) VALUES (?, ?)", 
                           (filme.titulo, filme.duracao))
            return cursor.lastrowid

    def listar(self):
        with Connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM filmes")
            return cursor.fetchall()