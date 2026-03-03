from flask import Blueprint, Flask, request, jsonify
from flask import render_template,request,redirect,url_for
from Servicos import Services

api_bp = Blueprint("api_bp",__name__)

sensores = [] # Lista para armazenar os dados dos sensores

@api_bp.route('/') #Rota principal para renderizar a página inicial

def principal():
    return render_template('paginahome.html')

@api_bp.route('/sensores', methods = ['GET']) #Rota para obter os dados dos sensores

def get_sensores():
    
    return jsonify({"sensores": sensores}), 200

@api_bp.route('/recebersensores', methods = ['POST']) #Rota para receber os dados dos sensores

def receber_sensores():
    
    data = request.get_json()

    resultado, status = Services.processar_dados(data)

    if status != 200:
        return jsonify(resultado), status

    sensores.append(data)

    return jsonify(resultado), 200

@api_bp.route('/selecionarsensor/<int:index>', methods = ['GET']) #Rota para selecionar um sensor específico com base no índice

def selecionar_sensor(index):
    if index >= 0 and index < len(sensores):
        return {"sensor": sensores[index]}, 200
    else:
        return {"message": "Sensor não encontrado!"}, 404
    
@api_bp.errorhandler(404) #Rota para lidar com erros 404
def not_found(error):
    return "Página não encontrada!", 404

#@app.route('/registro', methods = ['GET', 'POST']) #Rota para registrar um novo usuario(incompleto)



