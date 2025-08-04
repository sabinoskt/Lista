from src.util.lista_global import obter_lista

def obter_Listar(lista):
    global obter_lista
    obter_lista = lista
    salvar_arquivo(obter_lista)

def listar():
    if len(obter_lista) > 0:
        print("Lista:")
        for valor, exibirLista in enumerate(obter_lista, start=1):
            print(f"{valor} - {exibirLista}")
    else:
        print("\nNada para listar")
    
CAMINHO_ARQUIVO = "Bloco_de_nota.txt"
def salvar_arquivo(lista):
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        arquivo.write(str(lista))

def recuperar_arquivo():
    try:
        with open(CAMINHO_ARQUIVO, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("\nArquivo não encontrado")
