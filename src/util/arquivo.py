CAMINHO_ARQUIVO = "Bloco_de_nota.txt"

# obter_lista_arquivo = obter_lista

# Salvar toda a lista em arquivo
def salvar_arquivo(lista):
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        arquivo.write(str(lista) + '\n')


# Adicionar à lista já existente
# def adicionar_arquivo(lista):
#     with open(CAMINHO_ARQUIVO, 'a') as arquivo:
#         arquivo.write(str(lista))



# def executar_ler_arquivo():
#     global obter_lista_arquivo
#     try:
#         with open(CAMINHO_ARQUIVO, 'r') as arquivo:
#             conteudo = arquivo.read()
#             obter_lista_arquivo = ast.literal_eval(conteudo)
#             arquivo.close
#     except FileNotFoundError:
#         print("\nArquivo não encontrado. Criar nova lista")


# Ler o arquivo que foi salvo anteriormente
# def ler_arquivo():
#         print("Lista salva anteriormente:")
#         for valor, chave in enumerate(obter_lista_arquivo, start=1):
#             print(f"{valor} - {chave}")


# def listar_arquivo():
#     executar_ler_arquivo()
#     return obter_lista_arquivo
