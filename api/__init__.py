from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS

from .model import db

def create_app():
    app = Flask(__name__)
    load_dotenv()
    CORS(app)
    try:
        print(db)
    except Exception as e:
        print(e)

    # routes list
    from .routes import routes_list
    routes_list(app)

    @app.route('/')
    def hello_world():
        return 'hello world!'

    return app