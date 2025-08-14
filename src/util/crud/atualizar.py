from src.util.lista_global import obter_global_lista
from src.util.io import obter_conteudo
from src.util.crud.listar import listar
from src.util.comecar_01 import comecar_01

def atualizar():
    listar()
    lista = obter_global_lista()
    indice = int(obter_conteudo())
    comecar_01(indice, lista)
        