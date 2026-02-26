from flask import Flask
from routes import FlaskRoute


app = Flask(__name__)

# Registrar blueprints de rotas
#app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)