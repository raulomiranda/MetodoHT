from flask import Flask, jsonify

app = Flask(__name__)

# Seus dados de estatística
estatisticas_futebol = {
    "gols_por_jogo": 2.7,
    "vitorias_casa": 45,
    "vitorias_fora": 35
}

@app.route("/estatisticas")
def obter_estatisticas():
    # Retorna os dados em JSON, prontos para serem consumidos pelo seu site
    return jsonify(estatisticas_futebol)

# ... mais rotas para times, jogadores, etc.