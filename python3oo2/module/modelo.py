""" Here Program superclass """
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes
    
    def dar_likes(self):
        self._likes += 1
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

""" Here Filme class """
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'
        
""" Here Serie class """        
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'

""" Here Playlist class """
class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)

""" New objects """
vingadores  = Filme('vingadores - guerra infinita', 2018, 160)
tmep        = Filme('todo mundo em pânico', 1999, 100)
atlanta     = Serie('atlanta', 2018, 2)
demolidor   = Serie('demolidor', 2016, 2)

""" Invoke dar_likes method """
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

listinha = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', listinha)

""" Outputs """
print(f'Playlist: {playlist_fim_de_semana.nome.title()} | {len(playlist_fim_de_semana)} programas.')

for programa in playlist_fim_de_semana:
    print(programa)
