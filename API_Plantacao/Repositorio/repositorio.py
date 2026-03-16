#codigo para simular DB será substituido por um banco de dados real posteriormente
_sensores = []
def salvardados(dados):
    _sensores.append(dados)
    return "Dados salvos com sucesso!"
def listardados():
    return _sensores
def obter_dados(index):
    if index >= 0 and index < len(_sensores):
        return _sensores[index], 200
    else:
        return "Dados não encontrados!"