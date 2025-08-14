from flask import Flask
from src.util.arquivo import lista_bp, acrescente_bp, atualizar_bp, deletar_bp
# from src.util.encerrar import encerrar
# from src.util.io import obter_conteudo_da_resposta


app = Flask(__name__)

blueprint = [
    lista_bp, 
    acrescente_bp, 
    atualizar_bp,
    deletar_bp
]

for bp in blueprint:
    app.register_blueprint(bp)

def gerar_api():
# print("Deseja gerar API? S/N: ")
# resposta = obter_conteudo_da_resposta()
# if resposta.upper() == 'S':
    print("Gerando API...")
    app.run(host="localhost", port=8080, debug=True)
# elif resposta.upper() == 'N':
#     encerrar()
# else:
#     print("inválida! Digite apenas \'S\' ou \'N\'")

# gerar_api()
