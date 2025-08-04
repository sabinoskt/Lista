from src.util.crud.atualizar import obter_Lista_atualizar
from src.util.crud.deletar import obter_Lista_deletar
from src.util.crud.listar import obter_Listar


def criarLista():
    lista = []
    try:
        quantidade = int(input("Quantos itens deseja na lista: "))
        for qtd in range(1, quantidade + 1):
            criar = input(f"{qtd} - ")
            lista.append(criar)
    except ValueError:
        print("\nEscolha apenas um número de item")
    
    obter_Listar(lista)
    obter_Lista_atualizar(lista)
    obter_Lista_deletar(lista)
    