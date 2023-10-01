from models.config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm.exc import NoResultFound

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant')

    def __init__(self, name, address):
        self.name = name
        self.address = address

    @classmethod
    def get_by_id(cls, restaurant_id):
        try:
            return cls.query.get(restaurant_id)
        except NoResultFound:
            return None