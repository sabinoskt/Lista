from src.util.lista_global import obter_global_lista


def listar():
    print("Lista:")
    lista = obter_global_lista()
    if len(lista) > 0:
        for valor, chave in enumerate(lista, start=1):
            print(f"{valor} - {chave}")
    else:
        print("Nada para listar")
