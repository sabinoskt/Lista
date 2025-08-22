# import os
from src.recurso.menu import menu
from src.util.gerar_api import gerar_api
# from src.util.io import obter_input_num


# def main():
#     # sistema = ["Menu (AGENDA)", "API"]
#     # print("\n" + '=' * 3 + " Sistema de Lista " + '=' * 3)
#     # print("Escolha o modo de execução:")
#     # for i, sist in enumerate(sistema, start=1):
#     #     print(f"[{i}] {sist}")
#
#     # escolha = obter_input_num("Digite 1 ou 2:", minimo=1, maximo=len(sistema))
#
#     # if escolha == 1:
#     #     os.system("cls" if os.name == "nt" else "clear")
#         menu()
#     # elif escolha == 2:
    #     os.system("cls" if os.name == "nt" else "clear")
        # gerar_api()
    # else:
    #     print("Opção inválida! Execute novamente e escolha 1 ou 2")


if __name__ == "__main__":
    # menu()
    gerar_api()
