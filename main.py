from model.filme import Filme
from model.playlist import Playlist
from model.serie import Serie

filme = Filme('branca de neve', 1990, 160)
serie = Serie('friends', 1990, 500)
filme2 = Filme('todo mundo em pânico', 1990, 100)
serie2 = Serie('Demolidos', 2016, 2)

filme.add_like()
filme2.add_like()
serie.add_like()
serie2.add_like()
filme.add_like()

filmes_e_series = [filme, serie, filme2, serie2]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)
playlist_fim_de_semana.adicionar_na_playlist(Filme("a culpa das estrelas", 1990, 100))

print("____________________________________")
playlist_fim_de_semana.listar()
print("____________________________________")
playlist_fim_de_semana.remover_da_playlist("Demolidos")
print("____________________________________")
playlist_fim_de_semana.listar()