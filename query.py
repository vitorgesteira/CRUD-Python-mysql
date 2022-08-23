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