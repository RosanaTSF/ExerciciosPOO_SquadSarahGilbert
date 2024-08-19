from pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, nome: str, email: str, telefone: str, nacionalidade: str):
        super().__init__(nome, email)
        self.telefone = telefone
        self.nacionalidade = nacionalidade

    def __str__(self):
        return f"{super().__str__()} | Telefone: {self.telefone}, Nacionalidade: {self.nacionalidade}"