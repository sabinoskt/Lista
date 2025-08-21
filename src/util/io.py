def obter_input_num(prompt: str, minimo: int = None, maximo: int = None) -> int:
    while True:
        try:
            valor = int(input(f"{prompt} "))
            if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                print(f"Por favor, digite um número entre {minimo if minimo is not None else ''}"
                      f"{' e ' if minimo is not None and maximo is not None else ''}"
                      f"{maximo if maximo is not None else ''}")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Digite apenas números")


def obter_input_text(prompt: str) -> str:
    while True:
        valor = input(f"{prompt} ").split()
        if valor:
            return valor
        print("Entrada inválida! Não pode estar vazia")
