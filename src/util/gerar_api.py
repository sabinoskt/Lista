from flask import Flask
from src.util.arquivo import lista_bp, acrescente_bp, atualizar_bp, deletar_bp


app = Flask(__name__)

for bp in [lista_bp, acrescente_bp, atualizar_bp, deletar_bp]:
    app.register_blueprint(bp)


def gerar_api():
    print("Gerando API...")
    app.run(host="localhost", port=8080, debug=True)
