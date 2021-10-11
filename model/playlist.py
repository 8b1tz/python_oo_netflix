class Playlist:
    def __init__(self, nome, programas):
        self.__nome = nome
        self.__programas = programas

    def __getitem__(self, item):
        return self.__programas[item]


    @property
    def programas(self):
        return self.__programas

    def adicionar_na_playlist(self, programa):
        self.__programas.append(programa)
        print("foi adicionado")

    def remover_da_playlist(self, nome):
        index = -1
        for programa in self.__programas:
            index += 1
            print(f"aqui {programa._nome}")
            if programa._nome == nome:
                self.__programas.pop(index)
                print("Removido com sucsso!")

    def listar(self):
        for programa in self.__programas:
            print(programa)

    def __len__(self):
        return len(self.__programas)