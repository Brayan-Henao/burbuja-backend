from flask import Flask
from app.config import Config


def crear_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route ("/health")
    def health():
        return{
            "status": "ok",
            "mensaje": "Burbuja backend funcionando"
        }
    return app