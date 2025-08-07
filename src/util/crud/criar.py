from src.util.arquivo import salvar_arquivo
from src.util.crud.adicionar import obter_lista_adicionar
from src.util.crud.atualizar import obter_lista_atualizar
from src.util.crud.deletar import obter_lista_deletar
from src.util.crud.listar import obter_listar
from src.util.io import obter_conteudo_criar, obter_conteudo_qtd
from src.util.lista_global import obter_global_lista


def criar_lista():
    lista = []
    try:
        quantidade = int(obter_conteudo_qtd())
        for qtd in range(1, quantidade + 1):
            criar = obter_conteudo_criar(qtd)
            lista.append(criar)
        obter_global_lista(lista)
    except ValueError:
        print("\nEscolha apenas um número de item")
    
    obter_listar(lista)
    obter_lista_atualizar(lista)
    obter_lista_deletar(lista)
    obter_lista_adicionar(lista)
    # salvar_arquivo(lista)
