from src.util.io import obter_conteudo_criar, obter_conteudo_qtd
from src.util.lista_global import obter_lista


def criar_lista():
    lista = []
    try:
        quantidade = int(obter_conteudo_qtd())
        for qtd in range(1, quantidade + 1):
            criar = obter_conteudo_criar(qtd)
            lista.append(criar)
        obter_lista(lista)
    except ValueError:
        print("\nEscolha apenas um número de item")
