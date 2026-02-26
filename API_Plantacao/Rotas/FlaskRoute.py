from flask import Flask, request
from flask import render_template,request,redirect,url_for

app = Flask(__name__)

sensores = [] # Lista para armazenar os dados dos sensores

@app.route('/') #Rota principal para renderizar a página inicial

def principal():
    return render_template('paginahome.html')

@app.route('/sensores', methods = ['GET']) #Rota para obter os dados dos sensores

def get_sensores():
    return {"sensores": sensores}

@app.route('/recebersensores', methods = ['POST']) #Rota para receber os dados dos sensores

def receber_sensores():
    data = request.get_json()
    sensores.append(data)
    return {"message": "Sensor recebido com sucesso!"}, 200

@app.route('/selecionarsensor/<int:index>', methods = ['GET']) #Rota para selecionar um sensor específico com base no índice

def selecionar_sensor(index):
    if index >= 0 and index < len(sensores):
        return {"sensor": sensores[index]}, 200
    else:
        return {"message": "Sensor não encontrado!"}, 404
    
@app.route('/registro', methods = ['GET', 'POST']) #Rota para registrar um novo usuario(incompleto)

def registro():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = generate_password_hash(request.form['senha'])

        novousuario = Usuario(nome=nome, senha=senha)

        return redirect(url_for('principal'))

