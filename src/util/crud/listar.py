from src.util.lista_global import obter_global_lista

def listar():
    obter_lista = obter_global_lista()
    if len(obter_lista) > 0:
        print("Lista:")
        for valor, exibirLista in enumerate(obter_lista, start=1):
            print(f"{valor} - {exibirLista}")
    else:
        print("\nNada para listar")
