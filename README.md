# CRUD-Python-mysql
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/vitorgesteira/exemplo-readme/edit/master/README.md)

# Sobre o projeto
Crud com python usando o mysql.connector

Aplicação feita com o intuito de treinar e aprender a desenvolver um crud com python usando o mysql.connector.
E tambem ter um modelo onde possa usar e adaptar em projetos futuros com python.

obs: uma classe DB onde faz a conexao com o banco de dados e um metodo ExecuteSQL() que recebe qualquer Query 

arquivo db.py
```python
class DB:
    dotenv.load_dotenv(dotenv.find_dotenv())
    def __init__(self):
        host = os.getenv("HOST")
        user = os.getenv("USER")
        password = os.getenv("PASSWORD")
        database = os.getenv("DATABASE")

        try:
            self.__conexao = mysql.connector.connect(host=host, user=user, password=password, database=database)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def ExecuteSQL(self, sql, select=False):
        try:
            cursor = self.__conexao.cursor()
            cursor.execute(sql)
            if not select:
                self.__conexao.commit()
            return cursor
        except Error as err:
            print("SQL Error: ", err)
            return False

```

obs: arquivo query.py com algumas querys que envia para o metodo ExecuteSQL() da classe DB

arquivo query.py
```python
from db import DB

db = DB()

def InsertSQL(usuario):
    sql = "INSERT INTO usuario (nome, email, senha)" \
          "VALUES ('%(nome)s', '%(email)s', '%(senha)s')"
    result = db.ExecuteSQL(sql % usuario)
    if result:
        print("Registro incluído!")

def UpdateSQL(usuario):
    sql = "UPDATE usuario SET nome='%(setNome)s', email='%(setEmail)s', senha='%(setSenha)s' " \
          "WHERE nome='%(whereNome)s'"
    result = db.ExecuteSQL(sql % usuario)
    if result:
        print("Alteração concluida!")

def removeSQL(usuario):
    sql = "DELETE FROM usuario WHERE nome = '%(nome)s'"
    result = db.ExecuteSQL(sql % usuario)
    if result:
        print("Usuario deletado!")

def selectSQL():
    sql = "SELECT * FROM usuario"
    result = db.ExecuteSQL(sql, True)
    for x in result:
        print(x)
```



# Tecnologias utilizadas
- Python
- Mysql.conector
- os

Pré-requisitos: Python 3 / pip / Mysql / os / dotenv
