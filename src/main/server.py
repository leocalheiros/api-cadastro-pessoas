from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from src.main.config.config import Config
from src.main.config.database import db


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db.init_app(app)

from .routes import person_blueprint
app.register_blueprint(person_blueprint)
