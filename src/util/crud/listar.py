from src.util.lista_global import ListaGlobal


def listar(lista_global: ListaGlobal):
    print("Lista:")
    lista = lista_global.get_lista()
    if lista:
        for i, item in enumerate(lista, start=1):
            print(f"{i} - {item}")
    else:
        print("Nada para listar")
