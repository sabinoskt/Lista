from util.io import obter_conteudo
from util.crud.listar import listar
from util.response import atualizar_response
from util.lista_global import obter_lista

def obter_Lista_atualizar(lista):
    global obter_lista
    obter_lista = lista

def atualizar():
    if len(obter_lista) > 0:
        listar()
        print("\nEscolha os itens que deseja atualizar na lista")
        try:
            opcao_int = int(obter_conteudo())
            indice = opcao_int
            if 0 <= indice <= len(obter_lista):
                obter_lista[opcao_int] = atualizar_response(obter_lista, opcao_int)
            else:
                print("Índice inválido")
        except ValueError:
            print("Digite um número válido")
    else:
        print("Nada listado para atualizar")
