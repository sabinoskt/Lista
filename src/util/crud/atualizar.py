from src.util.lista_global import ListaGlobal
from src.util.io import obter_input_num, obter_input_text
from src.util.crud.listar import listar


def atualizar(lista_global: ListaGlobal):
    if lista_global.esta_vazia():
        print("A lista está vazia, nada para atualizar")
        return

    listar(lista_global)
    indice = obter_input_num("Digite o número do item que deseja atualizar:", minimo=1, maximo=len(lista_global.get_lista()))
    novo_item = obter_input_text("Digite o novo item: ")

    if lista_global.atualizar_item(indice, novo_item):
        print("\nItem atualizado com sucesso")
    else:
        print("\nÍndice inválido")
