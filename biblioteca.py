from flask import Flask, render_template, request

app = Flask(__name__)


class Livro:
    def __init__(self, nome, autor, editora, ISBN, nr_paginas, categoria):
        self.nome = str(nome).title()
        self.autor = str(autor).title()
        self.editora = str(editora).title()
        self.isbn = str(ISBN)
        self.nr_paginas = int(nr_paginas)
        self.categoria = str(categoria).title()

    '''@property
    def nome(self):
        return self._nome
    @property
    def autor(self):
        return self._autor
    @property
    def editora(self):
        return self._autor
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
'''


book1 = Livro('introdução ao gitHub','paper bell & brent Beer','novatec','978-85-7522-414-4',133,'')
book2 = Livro('teste','teste','teste','teste',155,'teste')

#print(book1)
#print(book2)

lista = [book1, book2]

@app.route('/teste')
def index():
    return render_template('index.html', titulo = 'Biblioteca', biblioteca=lista)

app.run(debug=True)