from app import app
from models.config import db  # Replace 'your_app' with the actual name of your Flask app
from models.restaurants import Restaurant   # Import your models
from models.pizzas import Pizza
from models.restaurant_pizzas import RestaurantPizza
# Create a Flask app context
app.app_context().push()

# Create or drop and recreate tables
db.drop_all()
db.create_all()

# Seed your database with initial data
def seed_database():
    # Create Restaurants
    restaurant1 = Restaurant(name="Sottocasa NYC", address="298 Atlantic Ave, Brooklyn, NY 11201")
    restaurant2 = Restaurant(name="PizzArte", address="69 W 55th St, New York, NY 10019")

    # Create Pizzas
    pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    # Create RestaurantPizzas (relationships)
    restaurant_pizza1 = RestaurantPizza(price=12.99, restaurant=restaurant1, pizza=pizza1)
    restaurant_pizza2 = RestaurantPizza(price=14.99, restaurant=restaurant1, pizza=pizza2)
    restaurant_pizza3 = RestaurantPizza(price=11.99, restaurant=restaurant2, pizza=pizza1)

    # Add data to the session
    db.session.add(restaurant1)
    db.session.add(restaurant2)
    db.session.add(pizza1)
    db.session.add(pizza2)
    db.session.add(restaurant_pizza1)
    db.session.add(restaurant_pizza2)
    db.session.add(restaurant_pizza3)

    # Commit the changes to the database
    db.session.commit()

if __name__ == "__main__":
    seed_database()
    print("Database seeded successfully.")