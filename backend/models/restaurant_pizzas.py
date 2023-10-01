from models.config import db
from sqlalchemy_serializer import SerializerMixin

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizza'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False, 
                    #   checkprice=db.CheckConstraint('price >= 1 AND price <= 30')
                      )
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    pizza = db.relationship('Pizza', back_populates='pizza_restaurants')
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')

    def __init__(self, price, restaurant, pizza):
        self.price = price
        self.restaurant = restaurant
        self.pizza = pizza