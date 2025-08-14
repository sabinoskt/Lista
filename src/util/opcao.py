from src.util.arquivo import salvar_arquivo
from src.util.crud.adicionar import adicionar
from src.util.crud.listar import listar
from src.util.crud.atualizar import atualizar
from src.util.crud.criar import criar_lista
from src.util.crud.deletar import deletar
from src.util.encerrar import encerrar
from src.util.io import obter_conteudo
from src.util.lista_global import obter_global_lista
import time
import os


def escolha_opcao(opcao):
    match opcao:
        case 1:
            os.system("cls")
            tabela = ["Criar nova lista", "Adicionar à lista existente"]
            print("Deseja criar uma nova lista ou adicionar itens a uma lista existente?")
            for num, text in enumerate(tabela, start=1):
                print(f"{num} - {text}")
            opcao_tabela = int(obter_conteudo())
            if opcao_tabela.__eq__(1):
                criar_lista()
            elif opcao_tabela.__eq__(2):
                lista_vazia = obter_global_lista()
                if len(lista_vazia) == 0:
                    print("Não é possível adicionar itens enquanto a lista estiver vazia")
                    time.sleep(3.0)
                else:
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
        case _:
            os.system("cls")
            print("\nEscolha apenas número a opção")
