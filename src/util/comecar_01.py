def comecar_01(indice, obter_lista):
    if 1 <= indice <= len(obter_lista):
        for i in range(1, len(obter_lista) + 1):
            if indice == i:
                obter_lista[i - 1] = input(f"{i} - ")
    else:
        print("\nÍndice inválido")
