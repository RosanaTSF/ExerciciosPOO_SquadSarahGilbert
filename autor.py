from pessoa import Pessoa

class Autor(Pessoa):
    def __init__(self, nome: str, email: str):
        super().__init__(nome, email)

    def __str__(self) -> str:
        return super().__str__()