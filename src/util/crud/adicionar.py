from sqlite.inserir import inserir
from sqlite.select import lista_select_vazia
# from src.util.io import obter_input_num, obter_input_text
from src.util.lista_global import ListaGlobal


def adicionar(lista_global: ListaGlobal):
    if lista_global.esta_vazia() and lista_select_vazia():
        print("Não é possível adicionar itens enquanto a lista estiver vazia")
        return
    
    # qtd = obter_input_num("Quantos itens deseja adicionar")
    # itens = []
    linha = int(input("Quantas linha(s) deseja adicionar?: "))
    for linhas in range(linha):
        carro = {
            "Modelo": input("Modelo: "),
            "Cor": input("Cor: "),
            "Ano": int(input("Ano: "))
        }
        inserir(carro["Modelo"], carro["Cor"], carro["Ano"])

    # for i in range(qtd):
    #     item = obter_input_text(f"{i} - ")
    #     # lista_global.adicionar_item(item)
    #     itens.append(item)
    # modelo, cor, ano = itens

    print("\nItens adicionados com sucesso!")
