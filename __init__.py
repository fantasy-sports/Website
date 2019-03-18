from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'db9439c2b827d2085562a1e0b4bee8bc' # secret key to protect forms from attacks - https://youtu.be/UIJKdCIEXUQ (10:20)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fancysite.db'
db = SQLAlchemy(app)

from fancyoptimizer import routes