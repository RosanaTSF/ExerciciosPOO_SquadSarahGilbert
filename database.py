from livro import Livro

def get_livros():
    return [
        Livro(
            lista_autor=[Autor('Josh Starmer PhD')],
            titulo='The StatQuest Illustrated Guide to Machine Learning!!!',
            editora='Packt Publishing',
            lista_genero=['Machine Learning','Statiscs'],
            lista_exemplar=['#01'],
            max_renovacao=1
        ),
        Livro(
            lista_autor=[Autor('Luciano Ramalho')],
            titulo='Python Fluente: Programação Clara, Concisa e Eficaz',
            editora='Novatec',
            lista_genero=['Programação'],
            lista_exemplar=['#01','#02'],
            max_renovacao=1
        ),
        Livro(
            lista_autor=[Autor('Robert C. Martin')],
            titulo='Código Limpo: Habilidades Práticas do Agile',
            editora='Alta Books',
            lista_genero=['Computação','Informática'],
            lista_exemplar=['#01','#02','#03'],
            max_renovacao=2
        ),
        Livro(
            lista_autor=[Autor('Nilo Ney Coutinho')],
            titulo='Introdução à Programação com Python',
            editora='Novatec',
            lista_genero=['Computação', 'Informática'],
            lista_exemplar=['#01', '#02', '#03'],
            max_renovacao=1
        ),
        Livro(
            lista_autor=[Autor('Henrique Bastos')],
            titulo='Python para Data Science',
            editora='Alta Books',
            lista_genero=['Ciência de Dados', 'Python', 'Machine Learning'],
            lista_exemplar=['#01', '#02', '#03'],
            max_renovacao=3
        ),
        Livro(
            lista_autor=[Autor('Eric Evans')],
            titulo='Domain-Driven Design: Desenvolvendo Software com Modelos de Domínio',
            editora='Casa do Código',
            lista_genero=['Arquitetura de Software', 'Design Patterns'],
            lista_exemplar=['#01'],
            max_renovacao=1
        ),
        Livro(
            lista_autor=[Autor('Martin Fowler')],
            titulo='Refactoring: Melhorando o Design de Código Existente',
            editora='Addison-Wesley',
            lista_genero=['Programação', 'Engenharia de Software'],
            lista_exemplar=['#01', '#02', '#03'],
            max_renovacao=3
        )
    ]
