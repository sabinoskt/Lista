from src.util.lista_global import obter_lista

def obter_Listar(lista):
    global obter_lista
    obter_lista = lista

def listar():
    if len(obter_lista) > 0:
        print("Lista:")
        for valor, exibirLista in enumerate(obter_lista, start=1):
            print(f"{valor} - {exibirLista}")
    else:
        print("\nNada para listar")
    