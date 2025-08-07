CAMINHO_ARQUIVO = "Bloco_de_nota.txt"

# Salvar toda a lista em arquivo
def salvar_arquivo(lista):
    with open(CAMINHO_ARQUIVO, 'w', encoding="UTF-8") as arquivo:
        arquivo.write(str(lista) + '\n')
