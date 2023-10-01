import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function RestaurantPizza() {
  const [restaurants, setRestaurants] = useState([]);
  const [pizzas, setPizzas] = useState([]);
  const [restaurantId, setRestaurantId] = useState("");
  const [pizzaId, setPizzaId] = useState("");
  const [price, setPrice] = useState("");
  const [formErrors, setFormErrors] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    // Fetch the list of restaurants
    fetch("/restaurants")
      .then((r) => r.json())
      .then((data) => setRestaurants(data));

    // Fetch the list of pizzas
    fetch("/pizzas")
      .then((r) => r.json())
      .then((data) => setPizzas(data));
  }, []);

  function handleSubmit(e) {
    e.preventDefault();
    const formData = {
      pizza_id: pizzaId,
      restaurant_id: restaurantId,
      price: parseInt(price),
    };
    fetch("/restaurant_pizzas", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    }).then((r) => {
      if (!r.ok) {
        // Handle the case where the response status is not OK (e.g., 400 or 500)
        throw new Error("Failed to add restaurant pizza");
      }
      return r.json();
    })
    .then((data) => {
      // Handle the successful response here
      navigate(`/restaurants/${restaurantId}`);
    })
    .catch((error) => {
      // Handle any errors that occurred during the fetch or JSON parsing
      setFormErrors([error.message]); console.log(formData)
    });
}
  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="pizza_id">Pizza:</label>
      <select
        id="pizza_id"
        name="pizza_id"
        value={pizzaId}
        onChange={(e) => setPizzaId(e.target.value)}
      >
        <option value="">Select a pizza</option>
        {pizzas.map((pizza) => (
          <option key={pizza.id} value={pizza.id}>
            {pizza.name}
          </option>
        ))}
      </select>
      <label htmlFor="restaurant_id">Restaurant:</label>
      <select
        id="restaurant_id"
        name="restaurant_id"
        value={restaurantId}
        onChange={(e) => setRestaurantId(e.target.value)}
      >
        <option value="">Select a restaurant</option>
        {restaurants.map((restaurant) => (
          <option key={restaurant.id} value={restaurant.id}>
            {restaurant.name}
          </option>
        ))}
      </select>
      <label htmlFor="price">Price:</label>
      <input
        type="text"
        id="price"
        name="price"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />
      {/* {formErrors.length > 0
        ? formErrors.map((err) => (
            <p key={err} style={{ color: "red" }}>
              {err}
            </p>
          ))
        : null} */}
      <button type="submit">Add Restaurant Pizza</button>
    </form>
  );
}

export default RestaurantPizza;
