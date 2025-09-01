from sqlite.delete import delete
from sqlite.select import lista_select_vazia, lista_select
from src.util.lista_global import ListaGlobal
from src.util.io import obter_input_num
from src.util.crud.listar import listar


def deletar(lista_global: ListaGlobal):
    if lista_global.esta_vazia() and lista_select_vazia():
        print("A lista está vazia, nada para deletar")
        return

    listar(lista_global)
    indice = obter_input_num("Digite o número item que  deseja deletar:")
    # item_removido = lista_global.deletar_item(indice)
    id_removido = delete(indice)

    if id_removido:
        print(f"\nVocê excluiu: {id_removido}")
    else:
        print("\nÍndice inválido")
