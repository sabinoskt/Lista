from util.io import obter_conteudo, obter_conteudo_da_resposta
from util.opcao import escolha_opcao
from util.message import continuar_ou_encerrar

def mostrarOpcao():
    crud = ["Criar", "Listar", "Atualizar", "Deletar"]
    print('-' * 20 + ' Menu ' + '-' * 20)
    print("Escolha a opção")
    for valor, crude in enumerate(crud, start=1):
        print(f"{valor} - {crude}")


def solicitacaoDeLista():
    while True:
        mostrarOpcao()
        opcao = obter_conteudo()
        escolha_opcao(opcao)
        continuar_ou_encerrar()
        encerrar = obter_conteudo_da_resposta().upper()
        if encerrar.__eq__('S'):
            exit()
            

def menu():
    solicitacaoDeLista()
