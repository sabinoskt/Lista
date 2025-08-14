import os
from src.util.arquivo import salvar_arquivo
# from src.util.gerar_api import gerar_api
from src.util.io import obter_conteudo
from src.util.lista_global import obter_global_lista
from src.util.opcao import escolha_opcao


def mostrarOpcao():
    crud = ["Criar", "Listar", "Atualizar", "Deletar", "Sair"]
    print(f"\n{'-' * 40}")
    print(f"{' ' * 17} MENU")
    print('-' * 40)
    print("\nEscolha a opção")
    for valor, crude in enumerate(crud, start=1):
        print(f"[{valor}] {crude}")


def solicitacaoDeLista():
    while True:
        mostrarOpcao()
        opcao = int(obter_conteudo())
        if opcao == 5:
            os.system("cls")
            lista = obter_global_lista()
            salvar_arquivo(lista)
            break
        escolha_opcao(opcao)
            

def menu():
    solicitacaoDeLista()


    # print("Gerar API?")
    #         resp = input("resp? S/N: ")
    #         if resp.upper() == 'S':
    #             gerar_api()
    #         elif resp.upper() == 'N':