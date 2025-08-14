from src.util.lista_global import obter_global_lista
from src.util.io import obter_conteudo
from src.util.deletar_comeca_01 import deletar_comeca_01
from src.util.crud.listar import listar


def deletar():
    listar()
    lista = obter_global_lista()
    indice = int(obter_conteudo())
    deletar_comeca_01(indice, lista)
