from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Livro:
    def __init__(self, nome, autor, editora, ISBN, nr_paginas, categoria):
        self._nome = str(nome).title()
        self._autor = str(autor).title()
        self._editora = str(editora).title()
        self._isbn = str(ISBN)
        self._nr_paginas = int(nr_paginas)
        self._categoria = str(categoria).title()

    @property
    def nome(self):
        return self._nome
    @property
    def autor(self):
        return self._autor
    @property
    def editora(self):
        return self._editora
    @property
    def isbn(self):
        return self._isbn
    @property
    def nr_paginas(self):
        return self._nr_paginas
    @property
    def categoria(self):
        return self._categoria

    def __str__(self):
        return (f'{self.nome} - {self.autor} - {self.editora} - {self.isbn} - {self.nr_paginas} - {self.categoria}')



book1 = Livro('introdução ao gitHub','paper bell & brent Beer','novatec','978-85-7522-414-4',133,'pROGRAMAÇÃO')
book2 = Livro('teste','teste','teste','teste',155,'teste')

#print(book1)
#print(book2)

lista = [book1, book2]

@app.route('/')
def index():
    return render_template('index.html', titulo = 'Biblioteca', biblioteca=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo = 'Adiciona livro')

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
    return redirect('/')

app.run(debug=True)