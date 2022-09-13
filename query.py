from db import DB

db = DB()

def InsertSQL(usuario):
    sql = "INSERT INTO usuario (nome, email, senha, data_criacao)" \
          "VALUES ('%(nome)s', '%(email)s', '%(senha)s', '%(data)s')"
    db.ExecuteSQL(sql % usuario)

def UpdateSQL(usuario):
    sql = "UPDATE usuario SET nome='%(setNome)s', email='%(setEmail)s', senha='%(setSenha)s' " \
          "WHERE nome='%(whereNome)s'"
    db.ExecuteSQL(sql % usuario)

def removeSQL(usuario):
    sql = "DELETE FROM usuario WHERE nome = '%(nome)s'"
    db.ExecuteSQL(sql % usuario)
    

def selectSQL():
    sql = "SELECT * FROM usuario"
    result = db.ExecuteSQL(sql, True)
    return result

def selectByIdSQL(pk):
    sql = "SELECT * FROM usuario WHERE id_usuario=%(pk)s" % {'pk': pk}
    result = db.ExecuteSQL(sql, True)
    return result.fetchone()