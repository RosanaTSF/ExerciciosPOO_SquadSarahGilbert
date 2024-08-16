from abc import ABC, abstractmethod #para ser uma classe abstrata - não pode ser instaciada (não possui objetos próprios dela)
import uuid #para atribuicao de ids as pessoas do nosso database
import random

rd = random.Random()
rd.seed(123)
class Pessoa(ABC):
    def __init__(self, id, nome: str, email: str):
        self.__id = str(uuid.UUID(int=rd.getrandbits(128), version=4))
        self._nome = nome
        self.email = email

    def __str__(self) -> str:
        return f"Nome: {self.nome} | E-mail: {self.email}"
    
    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def email(self):
        return self.email
    
    @email.setter #importante caso a pessoa tenha mudado de email - recadastro
    def email(self, novo_email): 
        self.email = novo_email