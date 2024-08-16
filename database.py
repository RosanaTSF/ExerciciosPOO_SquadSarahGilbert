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
    return [
        Livro(
            lista_autor=[get_autores()[0]],
            titulo='The StatQuest Illustrated Guide to Machine Learning!!!',
            editora='Packt Publishing',
            lista_genero=['Machine Learning','Statiscs'],
            lista_exemplar=['#01'],
            max_renovacao=1
        ),
        Livro(
            lista_autor=[get_autores()[1]],
            titulo='Python Fluente: Programação Clara, Concisa e Eficaz',
            editora='Novatec',
            lista_genero=['Programação'],
            lista_exemplar=['#01','#02'],
            max_renovacao=1
        ),
        Livro(
            lista_autor=[get_autores()[2]],
            titulo='Código Limpo: Habilidades Práticas do Agile',
            editora='Alta Books',
            lista_genero=['Computação','Informática'],
            lista_exemplar=['#01','#02','#03'],
            max_renovacao=2
        ),
        Livro(
            lista_autor=[get_autores()[3]],
            titulo='Introdução à Programação com Python',
            editora='Novatec',
            lista_genero=['Computação', 'Informática'],
            lista_exemplar=['#01', '#02', '#03'],
            max_renovacao=1
        ),
        Livro(
            lista_autor=[get_autores()[4], get_autores()[5], get_autores()[6]],
            titulo='Algoritmos e Programação de Computadores',
            editora='GEN LTC',
            lista_genero=['Computação', 'Informática', 'Mídias Digitais'],
            lista_exemplar=['#01', '#02', '#03'],
            max_renovacao=2
        )
    ]