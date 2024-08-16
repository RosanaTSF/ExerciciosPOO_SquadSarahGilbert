from Livro import Livro
from Autor import Autor

def get_autores():
    return [
        Autor(nome='Josh Starmer', email='joshstamer@gmail.com'),
        Autor(nome='Luciano Ramalho', email='lucianoramalho@gmail.com'),
        Autor(nome='Robert C. Martin', email='robertmartin@gmail.com'),
        Autor(nome='Nilo Ney Coutinho', email='neycoutinho@gmail.com'),
        Autor(nome='An Engelbrecht', email='anengelbrecht@gmail.com'),
        Autor(nome='Gilberto Nakamiti', email='gilbertonakamiti@gmail.com'),
        Autor(nome='Dilermando Junior', email='dilermandojr@gmail.com')
    ]

def get_livros():
    lista_autores_sistema = get_autores()
    return [
        Livro(
            lista_autor=[lista_autores_sistema[0]],
            titulo='The StatQuest Illustrated Guide to Machine Learning!!!',
            editora='Packt Publishing',
            lista_genero=['Machine Learning','Statiscs'],
            lista_exemplar=['#01'],
            max_renovacao=1
        ),
        Livro(
            lista_autor=[lista_autores_sistema[1]],
            titulo='Python Fluente: Programação Clara, Concisa e Eficaz',
            editora='Novatec',
            lista_genero=['Programação'],
            lista_exemplar=['#01','#02'],
            max_renovacao=1
        ),
        Livro(
            lista_autor=[lista_autores_sistema[2]],
            titulo='Código Limpo: Habilidades Práticas do Agile',
            editora='Alta Books',
            lista_genero=['Computação','Informática'],
            lista_exemplar=['#01','#02','#03'],
            max_renovacao=2
        ),
        Livro(
            lista_autor=[lista_autores_sistema[3]],
            titulo='Introdução à Programação com Python',
            editora='Novatec',
            lista_genero=['Computação', 'Informática'],
            lista_exemplar=['#01', '#02', '#03'],
            max_renovacao=1
        ),
        Livro(
            lista_autor=[lista_autores_sistema[4:7]],
            titulo='Algoritmos e Programação de Computadores',
            editora='GEN LTC',
            lista_genero=['Computação', 'Informática', 'Mídias Digitais'],
            lista_exemplar=['#01', '#02', '#03'],
            max_renovacao=2
        )
    ]