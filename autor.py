from pessoa import Pessoa

class Autor(Pessoa):
    def __init__(self, id, nome: str, email: str):
        super().__init__(id, nome, email)

    def __str__(self) -> str:
        return f"Autor:\n{super().__str__()}"