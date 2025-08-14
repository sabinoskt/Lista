from src.util.lista_global import obter_lista
from src.util.io import obter_conteudo_qtd, obter_conteudo_criar


def criar_lista():
    lista = []
    qtd = int(obter_conteudo_qtd())
    for i in range(1, qtd + 1):
        criar = obter_conteudo_criar(i)
        lista.append(criar)
    obter_lista(lista)
        