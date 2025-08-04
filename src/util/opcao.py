from src.util.crud.listar import listar
from src.util.crud.atualizar import atualizar
from src.util.crud.criar import criarLista
from src.util.crud.deletar import deletar
from src.util.encerrar import encerrar


def escolha_opcao(opcao):
    
    match int(opcao):
        case 1:
            criarLista()
        case 2:
            listar()
        case 3:
            atualizar()
        case 4:
            deletar()
        case 5:
            encerrar()
        case _:
            print("\nEscolha apenas número a opção")
