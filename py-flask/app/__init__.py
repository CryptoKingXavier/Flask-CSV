from flask import Flask
from secrets import token_hex


def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.config["SECRET_KEY"] = token_hex(16)
    
    from .views import views
    app.register_blueprint(views)
    
    return app
