from flask import Flask, request
from flask import render_template

app = Flask(__name__)
sensores = []
@app.route('/')
def hello():
    return 'TesteAPI'
@app.route('/recebersensor', methods=['POST'])
def recebersensor():
    
    data = request.get_json()
    sensores.append(data)
    return {"message": "Sensor recebido com sucesso",
        "total": len(sensores) }

@app.route('/sensores', methods=['GET'])
def get_sensores():
    return sensores
@app.route("/ultimosensor", methods=['GET'])
def get_ultimo_sensor():
    if sensores:
        return sensores[-1]
    else:
        return {"message": "Nenhum sensor recebido ainda."}


if __name__ == '__main__':
    app.run(debug=True)