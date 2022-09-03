import query

def insert():
    print('Inserir Usuario')
    nome = str(input('Nome: '))
    email = str(input('Email: '))
    senha = str(input('Senha: '))
    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha
    }
    query.InsertSQL(usuario)

def update():
    print('Atualisar Usuario:')
    setNome = str(input('Nome: '))
    setEmail = str(input('Email: '))
    setSenha = str(input('Senha: '))
    whereNome = str(input('No usuario: '))
    usuario = {
        "setNome": setNome,
        "setEmail": setEmail,
        "setSenha": setSenha,
        "whereNome": whereNome
    }
    query.UpdateSQL(usuario)

def remove():
    print('Remover usuario:')
    nome = str(input('Nome do usuario a ser removido: '))
    usuario = {
        "nome": nome
    }
    query.removeSQL(usuario)

def select():
    print('Usuario:', end=' ')
    query.selectSQL()
