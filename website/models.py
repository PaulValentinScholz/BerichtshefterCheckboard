from . import db
from flask_login import UserMixin, current_user


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128))
    name = db.Column(db.String(128))
    berichtshefter = db.relationship('Berichtshefter')


class Berichtshefter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vonDatum = db.Column(db.Date, nullable=False)
    bisDatum = db.Column(db.Date, nullable=False)
    erstellt = db.Column(db.Boolean, default=False)
    hochgeladen = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

