from util.crud.listar import listar
from util.io import obter_conteudo
from util.lista_global import obter_lista


def obter_Lista_deletar(lista):
    global obter_lista
    obter_lista = lista


def deletar():
    if len(obter_lista) > 0:
        listar()
        print("\nQual item deseja excluir?")
        try:
            opcao_int = int(obter_conteudo())
            indice = opcao_int
            if 0 <= indice <= len(obter_lista):
                item_excluido = obter_lista[opcao_int]
                del obter_lista[opcao_int]
                print(f"Você escolheu excluir: {item_excluido}")
            else:
                print("Índice inválido")
        except ValueError:
            print("Digite um número válido")
    else:
        print("\nNão há nada na lista para excluir")
