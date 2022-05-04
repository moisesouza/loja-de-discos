import psycopg2 as db

class Config:
    def __init__(self):
        self.config = {
            "postgres": {
              "user": "postgres",
              "password": "admin",
              "host": "localhost",
              "port": "5432",
              "database": "Loja_de_Discos"
            }
        }

class Connection(Config):
    def __init__(self):
        Config.__init__(self)
        self.conn = None
        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print("Erro na conexão", e)
            exit(1)

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn

    @property
    def cursor(self):
        return self.cur

    def commit(self):
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def execute(self, sql, params=None):
        self.cur.execute(sql, params or ())

    def query(self, sql, params=None):
        self.cur.execute(sql, params or ())
        return self.fetchall()


class Person(Connection):
    def __init__(self):
        Connection.__init__(self)

#Criando um insert para inserir cadastro de um cliente
    def insert(self, *args):
        try:
            sql = "INSERT INTO cadastro_cliente (cpf, nomeComp, idade, nascimento, email, telefone) VALUES(%s, %s, %s, %s, %s, %s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro ao inserir", e)

    def delete(self, id):
        try:
            sql_s = f"SELECT * FROM cadastro_cliente WHERE id = {id} "
            if not self.query(sql_s):
                return "Registro não encontrado para deletar"
            sql_d = f"DELETE FROM cadastro_cliente WHERE id = {id}"
            self.execute(sql_d)
            self.commit()
            return "Registro deletado"
        except Exception as e:
            print("Erro ao deletar", e)



if __name__ == "__main__":
    person = Person()
    person.insert(54900840491, "cris", "23", "rec", "cris@", "81997745544")
    print('Cadastro efetuado com sucesso')
    person.delete(4)
    