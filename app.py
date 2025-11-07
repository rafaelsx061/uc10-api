from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "mensagem": "API UC10 funcionando com sucesso!",
        "status": "online"
    })

@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return jsonify({
        "a": a,
        "b": b,
        "resultado": a + b
    })

def sum_numbers(a, b):
    return a + b

def get_text():
    return "UC10 - Teste Automatizado"

if __name__ == "__main__":
    app.run()
    
