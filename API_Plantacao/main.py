from flask import Flask
from Rotas.FlaskRoute import api_bp


app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(api_bp)  # Registrar o blueprint antes de iniciar o aplicativo
    app.run(debug=True)
    