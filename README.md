# Flask Code Challenge - Pizza Restaurants

This project is a Flask backend application that handles Pizza Restaurant data with a React frontend application to test the API. The application allows you to manage Restaurants and Pizzas, create relationships between them, and perform CRUD operations.

## Table of Contents

- [Models](#models)
  - [Relationships](#relationships)
- [Validations](#validations)
- [Routes](#routes)
  - [GET /restaurants](#get-restaurants)
  - [GET /restaurants/:id](#get-restaurantsid)
  - [DELETE /restaurants/:id](#delete-restaurantsid)
  - [GET /pizzas](#get-pizzas)
  - [POST /restaurant_pizzas](#post-restaurant_pizzas)

## Models

The following relationships have been defined in the application:

### Relationships

- A `Restaurant` has many `Pizza`s through `RestaurantPizza`.
- A `Pizza` has many `Restaurant`s through `RestaurantPizza`.
- A `RestaurantPizza` belongs to a `Restaurant` and belongs to a `Pizza`.

### Validations

The `RestaurantPizza` model has the following validation:

- Must have a `price` between 1 and 30.

## Routes

The application provides the following routes, returning JSON data in the specified format:

### GET /restaurants

Returns a list of restaurants in the following format:

```json
[
  {
    "id": 1,
    "name": "Sottocasa NYC",
    "address": "298 Atlantic Ave, Brooklyn, NY 11201"
  },
  {
    "id": 2,
    "name": "PizzArte",
    "address": "69 W 55th St, New York, NY 10019"
  }
]
