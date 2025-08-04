from src.util.io import obter_conteudo
from src.util.opcao import escolha_opcao


def mostrarOpcao():
    crud = ["Criar", "Listar", "Atualizar", "Deletar", "Sair"]
    print('-' * 20 + ' Menu ' + '-' * 20)
    print("\nEscolha a opção")
    for valor, crude in enumerate(crud, start=1):
        print(f"{valor} - {crude}")


def solicitacaoDeLista():
    while True:
        mostrarOpcao()
        opcao = obter_conteudo()
        escolha_opcao(opcao)
            

def menu():
    solicitacaoDeLista()
