from src.util.log import LogFileMixin
from flask import jsonify, request, Blueprint
from src.util.lista_global import ListaGlobal
import json


CAMINHO_ARQUIVO = "Bloco_de_nota.txt"

lista_global = ListaGlobal()
log = LogFileMixin()

# Salvar toda a lista em arquivo
def salvar_arquivo(lista_global: ListaGlobal):
    with open(CAMINHO_ARQUIVO, 'w', encoding="UTF-8") as arquivo:
        json.dump(lista_global.get_lista(), arquivo)


def carregar_arquivo():
    try:
        with open(CAMINHO_ARQUIVO, 'r') as ler:
            tempjson = json.load(ler)
            lista_global.set_lista(tempjson)
            return tempjson
    except FileNotFoundError:
        print("Arquivo não encontrado")


carregar_arquivo()

lista_bp = Blueprint("lista", __name__)
acrescente_bp = Blueprint("acrescente", __name__)
atualizar_bp = Blueprint("atualizar", __name__)
deletar_bp = Blueprint("deletar", __name__)


@lista_bp.route("/lista", methods=["GET"])
def listar_arquivo():
    dados = lista_global.get_lista()
    if dados:
        return jsonify(dados)
    log.log_error("Lista não encontrado")
    return jsonify({"erro": "Lista não encontrado"}), 404


@acrescente_bp.route("/acrescente", methods=["POST"])
def criar_lista_arquivo():  
    novo_item = request.json
    if not novo_item:
        log.log_error("Nenhum dado enviado")
        return jsonify({"erro": "Nenhum dado enviado"}), 400
    
    lista_global.adicionar_item(novo_item)
    salvar_arquivo(lista_global)
    log.log_success("Item criada")
    return jsonify({"mensagem": "Item criada", "dados": novo_item}), 201


@atualizar_bp.route("/atualizar/<int:indice>", methods=["PUT"])
def atualizar_arquivo(indice):
    novo_valor = request.json
    if not novo_valor:
        log.log_error("Nenhum dado enviado")
        return jsonify({"erro": "Nenhum dado enviado"}), 400
    
    if lista_global.atualizar_item(indice + 1, novo_valor):
        salvar_arquivo(lista_global)
        log.log_success("Item atualizada")
        return jsonify({"mensagem": "Item atualizada"})
    log.log_error("Índice inválido")
    return jsonify({"erro": "Índice inválido"}), 404


@deletar_bp.route("/deletar/<int:indice>", methods=["DELETE"])
def deletar_arquivo(indice):
    removido = lista_global.deletar_item(indice + 1)
    if removido is not None:
        salvar_arquivo(lista_global)
        log.log_success("Item deletado")
        return jsonify({"mensagem": "Item deletado", "dados": removido})
    log.log_error("Índice inválido")
    return jsonify({"erro": "Índice inválido"}), 404
