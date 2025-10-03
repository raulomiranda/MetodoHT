# MetodoHT

Pequena API Flask que expõe estatísticas de futebol.

Requisitos
- Python 3.8+
- Dependências em `requirements.txt` (instale com `pip install -r requirements.txt`)

Start command recomendado para o Render (produção):

```
gunicorn --bind 0.0.0.0:$PORT main:app
```

Execução local (desenvolvimento):

1. Crie e ative um virtualenv

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Rode localmente:

```
python main.py
```

Notas
- Para produção prefira `gunicorn` em vez do servidor de desenvolvimento do Flask.
- Se usar variáveis de ambiente locais, crie um arquivo `.env` e instale `python-dotenv`.