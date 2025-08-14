from flask import jsonify, request, Blueprint
import json


CAMINHO_ARQUIVO = "Bloco_de_nota.txt"

# Salvar toda a lista em arquivo
def salvar_arquivo(dados):
    with open(CAMINHO_ARQUIVO, 'w', encoding="UTF-8") as arquivo:
        json.dump(dados, arquivo)


def ler_dados() -> list:
    try:
        with open(CAMINHO_ARQUIVO, 'r') as ler:
            return json.load(ler)
    except FileNotFoundError:
        print("Arquivo não encontrado")

lista = ler_dados()

lista_bp = Blueprint("lista", __name__)

@lista_bp.route("/lista", methods=["GET"])
def listar_arquivo():
    if len(lista) > 0:
        return jsonify(lista)
    return jsonify({"erro": "Lista não encontrado"}), 404


acrescente_bp = Blueprint("acrescente", __name__)

@acrescente_bp.route("/acrescente", methods=["POST"])
def criar_lista_arquivo():  
    criar = request.json
    lista.append(criar)
    salvar_arquivo(lista)
    return jsonify({"mensagem": "Tarefa criada", "dados": criar}), 200


atualizar_bp = Blueprint("atualizar", __name__)

@atualizar_bp.route("/atualizar/<int:indice>", methods=["PUT"])
def atualizar_arquivo(indice):    
    if 0 <= indice < len(lista):
        lista[indice] = request.json
        salvar_arquivo(lista)
        return jsonify({"mensagem": "Tarefa atualizada"})
    return jsonify({"erro": "Tarefa não encontrado"}), 404


deletar_bp = Blueprint("deletar", __name__)

@deletar_bp.route("/deletar/<int:indice>", methods=["DELETE"])
def deletar_arquivo(indice):
    if 0 <= indice < len(lista):
        del lista[indice]
        salvar_arquivo(lista)
        return jsonify({"mensagem": "Deletada concluida"})
    return jsonify({"erro": "Tarefa não encontrado"}), 404
