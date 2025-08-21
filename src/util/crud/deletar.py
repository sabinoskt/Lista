from src.util.lista_global import ListaGlobal
from src.util.io import obter_input_num
from src.util.crud.listar import listar


def deletar(lista_global: ListaGlobal):
    if lista_global.esta_vazia():
        print("A lista está vazia, nada para deletar")
        return

    listar(lista_global)
    indice = obter_input_num("Digite o número item que  deseja deletar:", minimo=1, maximo=len(lista_global.get_lista()))
    item_removido = lista_global.deletar_item(indice)

    if item_removido:
        print(f"\nVocê excluiu: {item_removido}")
    else:
        print("\nÍndice inválido")
