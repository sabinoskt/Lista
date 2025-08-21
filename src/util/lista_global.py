class ListaGlobal:
    def __init__(self):
        self._lista = []

    def set_lista(self, nova_lista: list):
        self._lista = nova_lista.copy()

    def get_lista(self) -> list:
        return self._lista.copy()

    def adicionar_item(self, item):
        self._lista.append(item)

    def atualizar_item(self, indice: int, novo_valor):
        if 1 <= indice <= len(self._lista):
            self._lista[indice - 1] = novo_valor
            return True
        return False

    def deletar_item(self, indice: int):
        if 1 <= indice <= len(self._lista):
            return self._lista.pop(indice - 1)
        return None

    def esta_vazia(self):
        return len(self._lista) == 0
