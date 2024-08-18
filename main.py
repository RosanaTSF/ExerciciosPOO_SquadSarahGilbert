# main.py
from autor import Autor
from livro import Livro
from pessoa import Pessoa
from biblioteca import Biblioteca
from database import get_livros, get_autores

def main():
    """
    Função principal que simula o funcionamento da biblioteca.
    """
    # Obtendo os autores e livros do banco de dados
    autores = get_autores()  # Obtém a lista de autores
    livros = get_livros()    # Obtém a lista de livros
    
    # Criando alguns usuários
    usuarios = [
        Pessoa(id=None, nome='Sarah Gilbert', email='sarahG@example.com'),
        Pessoa(id=None, nome='Squad', email='squad@example.com')
    ]
    
    # Criando a biblioteca com os livros e usuários
    biblioteca = Biblioteca(livros=livros, usuarios=usuarios)
    
    # Simulando um empréstimo
    usuario = usuarios[0]
    livro = livros[0]
    exemplar = livro.lista_exemplar[0]  # Seleciona um exemplar disponível
    
    print(f"Emprestando o exemplar '{exemplar}' do livro '{livro.titulo}' para o usuário '{usuario.nome}'...")
    biblioteca.registro_emprestimo(usuario=usuario, livro=livro, exemplar=exemplar)
    
    # Simulando a devolução
    print(f"\nDevolvendo o exemplar '{exemplar}' do livro '{livro.titulo}'...")
    biblioteca.registro_devolucao(usuario=usuario, livro=livro, exemplar=exemplar)

if __name__ == "__main__":
    main()
