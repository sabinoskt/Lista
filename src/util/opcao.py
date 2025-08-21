from src.util.crud.adicionar import adicionar
from src.util.crud.listar import listar
from src.util.crud.atualizar import atualizar
from src.util.crud.criar import criar_lista
from src.util.crud.deletar import deletar
from src.util.lista_global import ListaGlobal
import time
import os


def escolha_opcao(opcao: int, lista_global: ListaGlobal):
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case 1:
            criar_lista(lista_global)
        case 2:
            listar(lista_global)
        case 3:
            adicionar(lista_global)
        case 4:
            atualizar(lista_global)
        case 5:
            deletar(lista_global)
        case _:
            print("Opção inválida! Escolha um número válido")
            time.sleep(2)
