from models.config import db
from sqlalchemy_serializer import SerializerMixin

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizza'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)

    pizza_restaurants = db.relationship('RestaurantPizza', back_populates='pizza')

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
