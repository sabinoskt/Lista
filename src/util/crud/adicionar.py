# from src.util.arquivo import adicionar_arquivo
from src.util.io import obter_conteudo_adicionar, obter_conteudo_qtd
from src.util.lista_global import obter_global_lista


def obter_lista_adicionar(lista):
    obter_global_lista(lista)
    # adicionar_arquivo(obter_lista)


def adicionar():
    quantidade = int(obter_conteudo_qtd())
    for qtd in range(1, quantidade + 1):
        adicionar = obter_conteudo_adicionar(qtd)
        obter_global_lista().append(adicionar)
    # adicionar_arquivo(obter_lista)
    