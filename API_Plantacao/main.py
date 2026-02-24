import FlaskRoute as fr
from Modulos.Rotas.service_routes import validar_rota
from Servicos.Services import atualizar_sensores, validar_sensores, diganosticar_sensores
from flask import Flask