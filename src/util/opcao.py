from src.util.arquivo import salvar_arquivo
from src.util.crud.adicionar import adicionar
from src.util.crud.listar import listar
from src.util.crud.atualizar import atualizar
from src.util.crud.criar import criarLista
from src.util.crud.deletar import deletar
from src.util.encerrar import encerrar
from src.util.io import obter_conteudo
import os

def escolha_opcao(opcao):
    
    match int(opcao):
        case 1:
            os.system("cls")
            tabela = ["Criar nova lista", "Adicionar à lista existente"]
            print("Deseja criar uma nova lista ou adicionar itens a uma lista existente?")
            for num, text in enumerate(tabela, start=1):
                print(f"{num} - {text}")
            opcaoTabela = int(obter_conteudo())
            if opcaoTabela.__eq__(1):
                criarLista()
            elif opcaoTabela.__eq__(2):
                adicionar()
            else:
                print("\nOpção inválida. Por favor, selecione um número válido")
        case 2:
            os.system("cls")
            listar()
        case 3:
            os.system("cls")
            atualizar()
        case 4:
            os.system("cls")
            deletar()
        case 5:
            os.system("cls")
            salvar_arquivo()
            encerrar()
        case _:
            os.system("cls")
            print("\nEscolha apenas número a opção")
