from src.util.io import obter_conteudo_adicionar, obter_conteudo_qtd
from src.util.lista_global import obter_global_lista


def adicionar():
    add = obter_global_lista()
    qtd = int(obter_conteudo_qtd())
    for i in range(1, qtd + 1):
        new_add = obter_conteudo_adicionar(i)
        add.append(new_add)
