from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
# from .models import Stock
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://quant:123456@localhost/quant'
db = SQLAlchemy(app)
class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True)
    name = db.Column(db.String(20), unique=True)
    buttom = db.Column(db.FLOAT(10))
    top = db.Column(db.FLOAT(10))
    up = db.Column(db.FLOAT(10))
    down = db.Column(db.FLOAT(10))
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __repr__(self):
        return '<Stock %r>' % self.name

