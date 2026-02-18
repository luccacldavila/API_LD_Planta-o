temperatura = 0.0
umidade = 0.0
pressão = 0.0

def atualizar_sensores(temp, umid, press):
    global temperatura, umidade, pressão
    temperatura = temp
    umidade = umid
    pressão = press

def validar_sensores():
    if temperatura < 0 or temperatura > 0:
        return False
    if umidade < 0 or umidade > 100:
        return False
    if pressão < 900 or pressão > 1100:
        return False
    return True

def diganosticar_sensores():
    if(temperatura < 0 and pressão < 0 and umidade < 0):
        return "Todos os sensores estão com falha"
    elif(temperatura < 0 and pressão < 0 and umidade >= 0):
        return "Sensores de temperatura e pressão estão com falha"
    elif(temperatura < 0 and pressão >= 0 and umidade < 0):
        return "Sensores de temperatura e umidade estão com falha"
    elif(temperatura >= 0 and pressão < 0 and umidade < 0):
        return "Sensores de pressão e umidade estão com falha"
    elif(temperatura < 0 and pressão >= 0 and umidade >= 0):
        return "Sensor de temperatura está com falha"
    elif(temperatura >= 0 and pressão < 0 and umidade >= 0):
        return "Sensor de pressão está com falha"
    elif(temperatura >= 0 and pressão >= 0 and umidade < 0):
        return "Sensor de umidade está com falha"
    else:        return "Todos os sensores estão funcionando corretamente"