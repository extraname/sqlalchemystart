from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
