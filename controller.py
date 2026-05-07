from repository import FilmeRepository
from model import Filme

class FilmeController:
    def __init__(self):
        self.repo = FilmeRepository()

    def cadastrar(self, titulo, duracao):
        if not titulo or duracao <= 0:
            return False, "Dados inválidos!"
        
        novo_filme = Filme(titulo, duracao)
        self.repo.salvar(novo_filme)
        return True, "Filme cadastrado com sucesso!"

    def buscar_todos(self):
        return self.repo.listar()