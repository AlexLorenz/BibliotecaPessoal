from flask import Flask, render_template, request

app = Flask(__name__)


class Livro:
    def __init__(self, nome, autor, editora, ISBN, nr_paginas, categoria):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.isbn = ISBN
        self.nr_paginas = nr_paginas
        self.categoria = categoria
    '''@property
    def nome(self):
        return self.nome
        
    @property
    def autor(self):
        return self.autor
    @property
    def editora(self):
        return self.editora
    @property
    def isbn(self):
        return self.isbn
    @property
    def nr_paginas(self):
        return self.nr_paginas
    @property
    def categoria(self):
        return self.categoria'''
    def __str__(self):
        return (f'{self.nome} - {self.autor} - {self.editora} - {self.isbn} - {self.nr_paginas} - {self.categoria}')



book1 = Livro('introdução ao gitHub',
               'paper bell & brent Beer',
               'novatec',
              '978-85-7522-414-4',
              133,'')

print(book1)