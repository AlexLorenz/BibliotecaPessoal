class Usuario:
    def __init__(self, id, nome, senha):
        self._id = id
        self._nome = nome
        self._senha = senha

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def senha(self):
        return self._senha
