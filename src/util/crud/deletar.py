from src.util.crud.listar import listar
from src.util.deletar_comeca_01 import deletar_comeca_01
from src.util.io import obter_conteudo
from src.util.lista_global import obter_global_lista


def obter_lista_deletar(lista):
    obter_global_lista(lista)


def deletar():
    obter_lista = obter_global_lista()
    if len(obter_lista) > 0:
        listar()
        print("\nQual item deseja excluir?")
        try:
            indice = int(obter_conteudo())
            deletar_comeca_01(indice, obter_lista)
        except ValueError:
            print("\nDigite um número válido")
    else:
        print("\nNão há nada na lista para excluir")
