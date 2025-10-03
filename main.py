from flask import Flask, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()
db_username = os.getenv("db_username")
db_password = os.getenv("db_password")
uri = f"mongodb+srv://{db_username}:{db_password}@metodoht.qe0n0od.mongodb.net/?retryWrites=true&w=majority&appName=MetodoHT"
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection


app = Flask(__name__)

@app.route("/")
def home():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return "Connection to MongoDB successful!"
    except Exception as e:
        print(e)
        return str(e)



@app.route("/inserir_time", methods=["POST"])
def inserir_time_mongo():
    # Lógica para inserir um time no MongoDB
    return jsonify({"message": "Time inserido com sucesso!"}), 201

#listar o times e ligas no mongo db 


if __name__ == "__main__":
    # Em deploys (Render, Heroku) a porta é fornecida pela variável de ambiente PORT
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)