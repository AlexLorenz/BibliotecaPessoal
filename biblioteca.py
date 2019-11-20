


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



