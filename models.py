from ext import db, login_manager
from flask_login import UserMixin

class BaseModel:
    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()

class User(db.Model, BaseModel, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), unique= True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    role = db.Column(db.String(), default="guest")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    img = db.Column(db.String(), nullable=False, default="default_photo.jpg")


class Watch(db.Model):
    __tablename__ = "watches"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    price = db.Column(db.String(), nullable=False)
    img = db.Column(db.String(), nullable=False, default="default_photo.jpg")





