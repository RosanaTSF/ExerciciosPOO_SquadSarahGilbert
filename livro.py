import uuid
import random

rd = random.Random()
rd.seed(123)

class Livro:
    def __init__(self, lista_autor, titulo, editora, lista_genero, lista_exemplar, max_renovacao):
        self.__id = str(uuid.UUID(int=rd.getrandbits(128), version=4))
        self.lista_autor = lista_autor
        self.titulo = titulo
        self.editora = editora
        self.lista_genero = lista_genero
        self._lista_exemplar = lista_exemplar  # Usando o setter aqui
        self._max_renovacao = max_renovacao  # Usando o setter aqui

    @property
    def max_renovacao(self):
        return self._max_renovacao
    
    @max_renovacao.setter
    def max_renovacao(self, value):
        if value < 0:
            raise ValueError("O número máximo de renovações deve ser positivo.")
        self._max_renovacao = value

    @property
    def lista_exemplar(self):
        return self._lista_exemplar

    @lista_exemplar.setter
    def lista_exemplar(self, value):
        if not isinstance(value, list):
            raise TypeError("A lista de exemplares deve ser uma lista.")
        self._lista_exemplar = value

    @property
    def id(self):
        return self.__id

    def __repr__(self):
        return f'Titulo: {self.titulo} | Autores: {self.lista_autor} | Lista exemplares: {self._lista_exemplar} | Lista generos: {self.lista_genero} | Editora: {self.editora} | Número máximo de renovações: {self._max_renovacao}\n'
