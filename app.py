from unicodedata import name
from flask import (
    Flask, request, redirect, render_template
)
import db
import query as q

app_name = 'crud-python-mysql'

app = Flask(__name__)

conDB = db.DB()

endpoint = 'usuarios'

@app.route(f'/{endpoint}-create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        usuario = {
            'nome': request.form['nome'],
            'email': request.form['email'],
            'senha': request.form['senha']
        }
        q.InsertSQL(usuario)
        return redirect('/usuarios')
    return render_template('create-user.html')

@app.route(f'/{endpoint}', methods=['GET'])
def get_all():
    users = q.selectSQL()
    return render_template('list-all-user.html', users=users)
    
@app.route(f'/{endpoint}/<pk>', methods=['GET'])
def get_by_id(pk):
    user = q.selectByIdSQL(pk)
    return render_template('list-user.html', user=user)

@app.route(f'/{endpoint}-update/<pk>', methods=['GET', 'POST'])
def update(pk):
    user = q.selectByIdSQL(pk)
    if request.method == 'POST':
        data_form = {
            'setNome': request.form['field_name'],
            'setEmail': request.form['field_email'],
            'setSenha': request.form['field_senha'],
            'whereNome': request.form['field_name_antigo']
        }
        q.UpdateSQL(data_form)
        return redirect('/usuarios')
    return render_template('update-user.html', user=user)

@app.route(f'/{endpoint}-delete/<name>', methods=['GET'])
def delete(name):
    q.removeSQL(
        {
            'nome': name
        }
    )
    return redirect('/usuarios')

if __name__ == '__main__':
    app.rum()