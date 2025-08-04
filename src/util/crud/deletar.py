from src.util.crud.listar import listar
from src.util.deletar_comeca_01 import deletar_comeca_01
from src.util.io import obter_conteudo
from src.util.lista_global import obter_lista

def obter_Lista_deletar(lista):
    global obter_lista
    obter_lista = lista


def deletar():
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
