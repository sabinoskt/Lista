from util.crud.criar import criarLista
from util.crud.listar import listar
from util.crud.atualizar import atualizar
from util.crud.deletar import deletar
from util.encerrar import encerrar


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
            print("Escolha apenas número a opção")
