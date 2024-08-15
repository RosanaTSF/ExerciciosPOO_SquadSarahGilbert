from Pessoa import Pessoa
from Livro import Livro #ainda a ser implementada - so coloquei p n dar erro no __init__

class Autor(Pessoa):
    def __init__(self, id, nome: str, email: str, lista_livros: Livro):
        super().__init__(id, nome, email)
        self.lista_livros = lista_livros

    def __str__(self) -> str:
        return f"Autor:\n{super().__str__()} | Lista de livros: {self.lista_livros}"

    @property
    def lista_livros(self):
        return self.lista_livros
    
    #provavelmente implementar ainda metodos especificos p adicionar, editar e remover a lista de livros do autor - mas acredito que deveriam ser de alguma outra classe
