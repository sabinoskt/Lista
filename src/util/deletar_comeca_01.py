def deletar_comeca_01(indice, obter_lista):
    try:
        item_excluido = obter_lista[indice - 1]
        if 1 <= indice <= len(obter_lista):
            for i in range(1, len(obter_lista) + 1):
                if indice == i:
                    del obter_lista[i - 1]
                    print(f"\nVocê escolheu escluir: {item_excluido}")
        else:
            print("\nÍndice inválido")
    except IndexError:
        print("\nÍndice inválido")
        