from model.netflix import Netflix


class Serie(Netflix):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self._ano} - {self.__temporadas}"

    def __eq__(self, other):
        return self._nome == other._nome



