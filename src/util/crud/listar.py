from sqlite.select import lista_select
from src.util.arquivo import carregar_arquivo
from src.util.lista_global import ListaGlobal


def listar(lista_global: ListaGlobal):
    print("Lista:")
    lista1 = lista_global.get_lista()
    lista2 = carregar_arquivo()
    lista3 = lista_select()

    lista = lista1 if lista1 else lista2

    if len(lista) == 0:
        lista = lista3

    if lista:
        for i, item in enumerate(lista, start=1):
            print(f"{i} - {item}")
    else:    
        print("Nada para listar")
