from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_restful import Api
from models.config import db
from models.pizzas import Pizza
from models.restaurants import Restaurant
from models.restaurant_pizzas import RestaurantPizza


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

@app.route('/')
def home():
    return 'Hello Flask App'

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_data = [
        {'id': restaurant.id, 
         'name': restaurant.name, 
         'address': restaurant.address}
        for restaurant in restaurants
    ]
    return jsonify(restaurant_data)

@app.route('/restaurants/<int:restaurants_id>', methods=['GET'])
def get_single_restaurant(restaurants_id):
    try:
        restaurant=Restaurant.query.get(restaurants_id)
        if restaurant:
            restaurant_info = {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address
            }
            return jsonify(restaurant_info)
        else:
            return jsonify({'error': 'Restaurant not found'}), 404
    except Exception as exception:
        return jsonify({'error': 'An error occurred'}), 500

@app.route('/pizzas', methods=['GET'])
def get_pizza():
    pizzas = Pizza.query.all()
    pizza_data = [
        {'id': pizza.id,
         'name': pizza.name,
         'ingredients': pizza.ingredients}
        for pizza in pizzas
    ]
    return jsonify(pizza_data)

@app.route('/pizzas/<int:pizza_id>', methods=['GET'])
def get_single_pizza(pizza_id):
    try:
        pizza = Pizza.query.get(pizza_id)
        if pizza:
            pizza_data = {
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            }
            return jsonify(pizza_data)
        else:
            return jsonify({'error': 'Pizza not found'}), 404
    except Exception as exception:
        return jsonify({'error': 'An error occurred'}), 500

@app.route('/restaurant_pizzas', methods=['GET'])
def get_restaurants_pizza():
    restaurant_pizza = RestaurantPizza.query.all()
    res_pizza = [
        {'id': res.id,
         "price":res.price,
         'pizza_id': res.pizza_id,
         'restaurant_id': res.restaurant_id}
         for res in restaurant_pizza
    ]
    return jsonify(res_pizza)

@app.route('/restaurant_pizzas/<int:pizza_id>', methods = ['GET'])
def get_single_restaurant_pizza(pizza_id):
    try:
        pizza = RestaurantPizza.query.get(pizza_id)
        if pizza:
            res_data = {
                'id': pizza.id,
                'price': pizza.price,
                'restaurant_id': pizza.restaurant_id,
                'pizza_id': pizza.pizza_id
            }
            return jsonify(res_data)
        else:
            return jsonify({'error': 'Restaurant not found'}),404
    except Exception as exception:
        return jsonify({'error': 'An error occurred'}), 500

@app.route('/pizzas', methods=['POST'])
def create_pizza():
    try:
        # Parse JSON data from the request body
        data = request.get_json()

        # Extract pizza details from the JSON data
        name = data.get('name')
        ingredients = data.get('ingredients')

        # Validate that both 'name' and 'ingredients' are provided
        if not name or not ingredients:
            return jsonify({'error': 'Both name and ingredients are required'}), 400

        # Create a new pizza instance
        pizza = Pizza(name=name, ingredients=ingredients)

        # Add the new pizza to the database
        db.session.add(pizza)
        db.session.commit()

        # Return a success response with the created pizza's details
        return jsonify({
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }), 201  # 201 Created status code

    except Exception as exception:
        return jsonify({'error': 'An error occurred'}), 500

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    try:
        data = request.get_json()

        # Extract data from JSON request
        price = data['price']
        pizza_id = data['pizza_id']
        restaurant_id = data['restaurant_id']

        # Validate price (assuming price is a float)
        if not (1 <= price <= 30):
            return jsonify({'error': 'Price must be between 1 and 30.'}), 400

        # Check if the specified Pizza and Restaurant exist
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if not (pizza and restaurant):
            return jsonify({'error': 'Pizza or Restaurant not found.'}), 404

        # Create a new RestaurantPizza record
        restaurant_pizza = RestaurantPizza(price=price, pizza=pizza, restaurant=restaurant)
        db.session.add(restaurant_pizza)
        db.session.commit()
        
        return jsonify({
            'id': restaurant_pizza.id,
            'price': restaurant_pizza.price,
            'pizza_id': restaurant_pizza.pizza_id,
            'restaurant_id': restaurant_pizza.restaurant_id
        }), 201

    except Exception as e:
        return jsonify({'error': 'An error occurred'}), 500
    
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    try:
        # Check if the restaurant exists
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return jsonify({'error': 'Restaurant not found'}), 404

        # Delete associated RestaurantPizza records
        restaurant_pizzas = RestaurantPizza.query.filter_by(restaurant_id=id).all()
        for restaurant_pizza in restaurant_pizzas:
            db.session.delete(restaurant_pizza)

        # Delete the restaurant itself
        db.session.delete(restaurant)
        db.session.commit()

        # Return a successful response
        return '', 204  # 204 No Content

    except Exception as e:
        return jsonify({'error': 'An error occurred'}), 500
                        
if __name__ == '__main__':
    app.run(debug=True, port = 5555)
