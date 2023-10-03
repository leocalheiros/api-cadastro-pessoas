from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from src.main.config.config import Config
from .routes import person_blueprint

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
app.register_blueprint(person_blueprint)
