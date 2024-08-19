from livro import Livro
from autor import Autor
from usuario import Usuario

def get_usuarios():
    return [
        Usuario("Jéssica Lizar", "jessicalizar@gmail.com", "12345678910", "Brasileira"),
        Usuario("Letícia Almeida", "leticiaalmeida@gmail.com", "10987654321", "Brasileira"),
        Usuario("Lívia Boscolo", "liviaboscolo@gmail.com", "12345109876", "Brasileira"),
        Usuario("Michelle Martins", "michellemartins@gmail.com", "10987612345", "Brasileira"),
        Usuario("Nadiveth Duno", "nadivethduno@gmail.com", "678910123456", "Venezuelana"),
        Usuario("Raquel Maia", "raquelmaaia@gmail.com", "54321109876", "Brasileira"),
        Usuario("Rosana Francisco", "rosanafrancisco@gmail.com", "54321678923", "Brasileira")
    ]

def get_autores():
    return [
        Autor(nome='Josh Starmer', email='joshstamer@gmail.com'),
        Autor(nome='Luciano Ramalho', email='lucianoramalho@gmail.com'),
        Autor(nome='Robert C. Martin', email='robertmartin@gmail.com'),
        Autor(nome='Nilo Ney Coutinho', email='neycoutinho@gmail.com'),
        Autor(nome='An Engelbrecht', email='anengelbrecht@gmail.com'),
        Autor(nome='Gilberto Nakamiti', email='gilbertonakamiti@gmail.com'),
        Autor(nome='Dilermando Junior', email='dilermandojr@gmail.com'),
        Autor(nome='Henrique Bastos', email='henriquebastos@gmail.com'),
        Autor(nome='Eric Evans', email='ericevans@gmail.com'),
        Autor(nome='Martin Fowler', email='martinfowler@gmail.com')
    ]

def get_livros():
    lista_autores_sistema = get_autores()
    return [
        Livro(
            lista_autor=[lista_autores_sistema[0].__str__()],
            titulo='The StatQuest Illustrated Guide to Machine Learning!!!',
            editora='Packt Publishing',
            lista_genero=['Machine Learning','Statiscs'],
            lista_exemplar=['#01'],
            max_renovacao=1
        ),
        Livro(
            lista_autor=[lista_autores_sistema[1].__str__()],
            titulo='Python Fluente: Programação Clara, Concisa e Eficaz',
            editora='Novatec',
            lista_genero=['Programação'],
            lista_exemplar=['#01','#02'],
            max_renovacao=1
        ),
        Livro(
            lista_autor=[lista_autores_sistema[2].__str__()],
            titulo='Código Limpo: Habilidades Práticas do Agile',
            editora='Alta Books',
            lista_genero=['Computação','Informática'],
            lista_exemplar=['#01','#02','#03'],
            max_renovacao=2
        ),
        Livro(
            lista_autor=[lista_autores_sistema[3].__str__()],
            titulo='Introdução à Programação com Python',
            editora='Novatec',
            lista_genero=['Computação', 'Informática'],
            lista_exemplar=['#01', '#02', '#03'],
            max_renovacao=1
        ),
        Livro(
            lista_autor=[lista_autores_sistema[4].__str__(), lista_autores_sistema[5].__str__(), lista_autores_sistema[6].__str__()],
            titulo='Algoritmos e Programação de Computadores',
            editora='GEN LTC',
            lista_genero=['Computação', 'Informática', 'Mídias Digitais'],
            lista_exemplar=['#01', '#02', '#03'],
            max_renovacao=2
        ),
        Livro(
            lista_autor=[lista_autores_sistema[7].__str__()],
            titulo='Python para Data Science',
            editora='Alta Books',
            lista_genero=['Ciência de Dados', 'Python', 'Machine Learning'],
            lista_exemplar=['#01', '#02', '#03'],
            max_renovacao=3
        ),
        Livro(
            lista_autor=[lista_autores_sistema[8].__str__()],
            titulo='Domain-Driven Design: Desenvolvendo Software com Modelos de Domínio',
            editora='Casa do Código',
            lista_genero=['Arquitetura de Software', 'Design Patterns'],
            lista_exemplar=['#01'],
            max_renovacao=1
        ),
        Livro(
            lista_autor=[lista_autores_sistema[9].__str__()],
            titulo='Refactoring: Melhorando o Design de Código Existente',
            editora='Addison-Wesley',
            lista_genero=['Programação', 'Engenharia de Software'],
            lista_exemplar=['#01', '#02', '#03'],
            max_renovacao=3
        )
    ]
