# from sqlite.inserir import inserir
from sqlite.inserir import inserir
from src.util.lista_global import ListaGlobal
from src.util.io import obter_input_num, obter_input_text


def criar_lista(lista_global: ListaGlobal):
    qtd = obter_input_num("Quantos itens deseja na lista:")
    veiculos = []
    for i in range(qtd):
        item = obter_input_text(f"{i} -")
        # lista_global.adicionar_item(item)
        veiculos.append(item)

    modelo, cor, ano = veiculos
    inserir(modelo, cor, ano)
    print("\nLista criada com sucesso!")
    