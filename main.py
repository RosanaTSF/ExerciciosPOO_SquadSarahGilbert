from biblioteca import Biblioteca, 
from database import get_livros, get_autores, get_usuarios

def main():
    """
    Função principal que simula o funcionamento da biblioteca.
    """
    #Listas de autores, livros e usuarios do database
    autores = get_autores()  
    livros = get_livros()    
    usuarios = get_usuarios()
    
    #Criando a biblioteca com os livros e usuários
    biblioteca = Biblioteca(livros=livros, usuarios=usuarios)
    
    #Seleção de alguns elementos da biblioteca para testes
    usuario_simples = usuarios[0]
    livro_simples = livros[0]
    exemplar = livro_simples.lista_exemplar[0]  # Seleciona um exemplar disponível
    
    #Informações gerais sobre um livro e um usuário qualquer da biblioteca
    print(f"Informações gerais sobre o livro {livro_simples.titulo} da biblioteca:\n\n{livro_simples.__str__()}")
    print(f"\nInformações gerais sobre o usuário {usuario_simples._nome} da biblioteca:\n\n{usuario_simples.__str__()}")

    #Empréstimo de livro
    print(f"\nEmprestando o exemplar '{exemplar}' do livro '{livro_simples.titulo}' para o usuário '{usuario_simples.nome}'...")
    biblioteca.registro_emprestimo(usuario=usuario_simples, livro=livro_simples, exemplar=exemplar)
    
    #Devolução de livro
    print(f"\nDevolvendo o exemplar '{exemplar}' do livro '{livro_simples.titulo}'...")
    biblioteca.registro_devolucao(usuario=usuario_simples, livro=livro_simples, exemplar=exemplar)

    #Acessando a lista de autores de alguns livros
    livro_varios_autores = livros[4]
    print(f"\nLista de autor(es) do livro {livro_simples.titulo}: {livro_simples.lista_autor}")
    print(f"\nLista de autores do livro: {livro_varios_autores.titulo}: {livro_varios_autores.lista_autor}")

if __name__ == "__main__":
    main()
