from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class CountData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    in_count = db.Column(db.Integer)
    out_count = db.Column(db.Integer)
    date = db.Column(db.Date)


class AlertLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
