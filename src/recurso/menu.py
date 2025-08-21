import os
from src.util.arquivo import salvar_arquivo
from src.util.io import obter_input_num
from src.util.lista_global import ListaGlobal
from src.util.opcao import escolha_opcao


def mostrar_menu():
    opcoes = ["Criar", "Listar", "Adicionar", "Atualizar", "Deletar", "Sair"]
    print(f"\n{'-' * 40}")
    print(f"{' ' * 17} MENU")
    print('-' * 40)
    for i, opcao in enumerate(opcoes, start=1):
        print(f"[{i}] {opcao}")
    return len(opcoes)


def menu():
    lista_global = ListaGlobal()
    while True:
        qtd_opcoes = mostrar_menu()
        opcao = obter_input_num("Escolha a opção:", minimo=1, maximo=qtd_opcoes)

        if opcao == qtd_opcoes:
            os.system("cls" if os.name == "nt" else "clear")
            print("Saindo e salvando a lista...")
            salvar_arquivo(lista_global)
            break

        escolha_opcao(opcao, lista_global)
