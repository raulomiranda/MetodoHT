from flask import Flask, jsonify
import os

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


if __name__ == "__main__":
    # Em deploys (Render, Heroku) a porta é fornecida pela variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)