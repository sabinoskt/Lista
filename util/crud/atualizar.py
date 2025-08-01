from util.io import obter_conteudo
from util.crud.listar import listar
from util.lista_global import obter_lista
from util.comecar_01 import comecar_1

def obter_Lista_atualizar(lista):
    global obter_lista
    obter_lista = lista

def atualizar():
    if len(obter_lista) > 0:
        listar()
        print("\nEscolha os itens que deseja atualizar na lista")
        try:
            indice = int(obter_conteudo())
            comecar_1(indice, obter_lista)
        except ValueError:
            print("Digite um número válido")
    else:
        print("Nada listado para atualizar")
