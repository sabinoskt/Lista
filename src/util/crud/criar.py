# from src.util.arquivo import salvar_arquivo
from src.util.crud.adicionar import obter_lista_adicionar
from src.util.crud.atualizar import obter_Lista_atualizar
from src.util.crud.deletar import obter_Lista_deletar
from src.util.crud.listar import obter_Listar
from src.util.io import obter_conteudo_criar, obter_conteudo_qtd



def criarLista():
    lista = []
    try:
        quantidade = int(obter_conteudo_qtd())
        for qtd in range(1, quantidade + 1):
            criar = obter_conteudo_criar(qtd)
            lista.append(criar)
    except ValueError:
        print("\nEscolha apenas um número de item")
    
    obter_Listar(lista)
    obter_Lista_atualizar(lista)
    obter_Lista_deletar(lista)
    obter_lista_adicionar(lista)
    # salvar_arquivo(lista)
