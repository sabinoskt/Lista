from src.util.io import obter_input_num, obter_input_text
from src.util.lista_global import ListaGlobal


def adicionar(lista_global: ListaGlobal):
    if lista_global.esta_vazia():
        print("Não é possível adicionar itens enquanto a lista estiver vazia")
        return
    
    qtd = obter_input_num("Quantos itens deseja adicionar", minimo=1)
    for i in range(1, qtd + 1):
        item = obter_input_text(f"{i} - ")
        lista_global.adicionar_item(item)
    print("\nItens adicionados com sucesso!")
