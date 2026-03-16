import time
from Repositorio import repositorio

dispostivo = {
    "id": 1,
    "umidade": 0.0,
    "temperatura": 0.0,
    "pressao": 0.0
}
  

def iniciar_Dispositivo(dispositivo_conectado):

    id = 1
    umidade = 0.0
    temperatura = 0.0
    pressao = 0.0

    dispositivo_conectado["id"] = id
    dispositivo_conectado["umidade"] = umidade
    dispositivo_conectado["temperatura"] = temperatura
    dispositivo_conectado["pressao"] = pressao

    return{"status": "Funcionando", "umidade": umidade, "temperatura": temperatura, "pressao": pressao}
    
def validar_dados(dados): # Função para validar os dados recebidos dos sensores

    if dados["umidade"] is not None and dados["temperatura"] is not None and dados["pressao"] is not None:

        if dados["umidade"] >= 0 and dados["umidade"] <= 100 and dados["temperatura"] >= -40 and dados["temperatura"] <= 125 and dados["pressao"] >= 300 and dados["pressao"] <= 1100:
        
         return "Dados válidos!"
    else:
        return "Dados inválidos! Verifique os campos umidade, temperatura e pressão."
def normalizar_dados(dados): # Função para normalizar os dados recebidos dos sensores
    dados.umidade = round(dados.umidade, 2)
    dados.temperatura = round(dados.temperatura, 2)
    dados.pressao = round(dados.pressao, 2)
    return dados  
    

def processar_dados(dados): # Função para processar os dados recebidos dos sensores(ainda em produção)
                 if not dados:
                  return {"message": "JSON inválido"}, 400

                 if "umidade" not in dados or "temperatura" not in dados or "pressao" not in dados:
                    return {"message": "Campos obrigatorios ausentes"}, 400
                 
                 else:
                    repositorio.salvardados(dispostivo)
                    return {"message": "Dados processados com sucesso!"}, 200


                 
iniciar_Dispositivo(dispostivo) #funções para teste
validar_dados(dispostivo)
    
print(dispostivo["id"])
print(dispostivo["umidade"])
print(dispostivo["temperatura"])
print(dispostivo["pressao"])


    