from pessoa import Pessoa
import uuid
import random

rd = random.Random()
rd.seed(123) 

class Usuario(Pessoa):
    def __init__(self, id, nome, email, telefone, nacionalidade):
        super().__init__(nome, id, email)
        self.telefone=telefone
        self.nacionalidade=nacionalidade
      
    def __repr__(self):
        return f'Usuario | ID: {self.__id}, Nome: {self.nome}, Telefone: {self.telefone}, Nacionaldiade: {self.nacionalidade}\n'


