from flask import Flask,render_template, request, redirect, session, flash, url_for
from biblioteca import Livro

book1 = Livro('introdução ao gitHub','paper bell & brent Beer','novatec','978-85-7522-414-4',133,'pROGRAMAÇÃO')
book2 = Livro('teste','teste','teste','teste',155,'teste')

lista = [book1, book2]

app = Flask(__name__)

app.secret_key = 'alura'

@app.route('/')
def index():
    return render_template('index.html', titulo = 'Biblioteca', biblioteca=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', prixima=url_for('novo')))
    return render_template('novo.html', titulo='Adiciona livro')


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', titulo='Login', proxima=proxima)


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado')
    return redirect('/')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Não foi possível logar, tente novamente!')
        return redirect(url_for('login'))


@app.route('/adicionar', methods=['POST', ])
def adicionar():
    nome = request.form['nome']
    autor = request.form['autor']
    editora = request.form['editora']
    isbn = request.form['isbn']
    nr_paginas = request.form['nr_paginas']
    categoria = request.form['categoria']
    book = Livro(nome, autor, editora, isbn, nr_paginas, categoria)
    lista.append(book)
    return redirect(url_for('index'))


app.run(debug=True)