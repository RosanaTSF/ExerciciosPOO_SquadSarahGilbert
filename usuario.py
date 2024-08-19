from pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, id, nome: str, email: str, telefone: str, nacionalidade: str):
        super().__init__(id, nome, email)
        self.telefone = telefone
        self.nacionalidade = nacionalidade

    def __repr__(self):
        return f"Usuário:\n{super().__str__()} | Telefone: {self.telefone}, Nacionaldiade: {self.nacionalidade}"