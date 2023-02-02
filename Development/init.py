

from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
mob = Blueprint('app', url_prefix='/app')

app = Flask(__name__)
app.secret_key ='Private Key'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)
app.register_blueprint(mob)


from . import handler