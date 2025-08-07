from src.util.comecar_01 import comecar_1
from src.util.crud.listar import listar
from src.util.io import obter_conteudo
from src.util.lista_global import obter_global_lista


def atualizar():
    obter_lista = obter_global_lista()
    if len(obter_lista) > 0:
        listar()
        print("\nEscolha os itens que deseja atualizar na lista")
        try:
            indice = int(obter_conteudo())
            comecar_1(indice, obter_lista)
        except ValueError:
            print("\nDigite um número válido")
    else:
        print("\nNada listado para atualizar")
