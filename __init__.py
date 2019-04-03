from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt #importing Bcrypt video 6
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'db9439c2b827d2085562a1e0b4bee8bc' # secret key to protect forms from attacks - https://youtu.be/UIJKdCIEXUQ (10:20)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fancysite.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view ='login'
login_manager.login_message_category = 'info'

from fancyoptimizer import routes