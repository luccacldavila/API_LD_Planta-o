from flask import Flask, request
from flask import render_template

app = Flask(__name__)
sensores = []
@app.route('/')
def principal():
    return render_template('index.html')
@app.route('/sensores', methods = ['GET'])
def get_sensores():
    return {"sensores": sensores}

@app.route('/recebersensores', methods = ['POST'])
def receber_sensores():
    data = request.get_json()
    sensores.append(data)
    return {"message": "Sensor recebido com sucesso!"}, 200
@app.route('/selecionarsensor/<int:index>', methods = ['GET'])
def selecionar_sensor(index):
    if index < len(sensores):
        return {"sensor": sensores[index]}, 200
    else:
        return {"message": "Sensor não encontrado!"}, 404