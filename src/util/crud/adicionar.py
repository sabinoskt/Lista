from src.util.io import obter_conteudo_adicionar, obter_conteudo_qtd
from src.util.lista_global import obter_global_lista


def adicionar():
    append = obter_global_lista()
    quantidade = int(obter_conteudo_qtd())
    for qtd in range(1, quantidade + 1):
        adicionar = obter_conteudo_adicionar(qtd)
        append.append(adicionar)
