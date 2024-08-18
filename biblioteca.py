from emprestimo import Emprestimo

class Biblioteca:
    def __init__(self,livros,usuarios):
        self._livros=livros
        self._exemplares=livros
        self._usuarios=usuarios
        self.dict_emprestimos = {}


    # Emprestimo
    def check_emprestimo(self, usuario, livro):
        return self.dict_emprestimos.get(f'{usuario.id}-{livro.id}',None)

    def registro_emprestimo(self,usuario,livro, exemplar):
        emprestimo = self.check_emprestimo(usuario,livro)
        if emprestimo is None: #posso criar o emprestimo
            id = f'{usuario.id}-{livro.id}' 
            self.dict_emprestimos[id] = Emprestimo(livro=livro,usuario = usuario
                                                    ,exemplar = exemplar
                                              ,ndays=20)    
            
            idx = self.search_livro_user_idx(livro.id)
            self._exemplares[idx].lista_exemplar.remove(exemplar)
            print('Emprestimo realizado')
        else:
            emprestimo.renovar()

    def registro_devolucao(self,usuario,livro, exemplar):
        id = f'{usuario.id}-{livro.id}' 
        self.dict_emprestimos[id].devolver()

        idx = self.search_livro_user_idx(livro.id)
        self._exemplares[idx].lista_exemplar.append(exemplar)










