from model.netflix import Netflix


class Filme(Netflix):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self._ano} - {self.__duracao}"

    def __eq__(self, other):
        return self._nome == other._nome

