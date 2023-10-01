import React, { useEffect, useState } from "react";
import {  useParams, useNavigate } from "react-router-dom";

function Restaurant() {
  const [restaurant, setRestaurant] = useState(null);
  const [error, setError] = useState(null);
  const [status, setStatus] = useState("pending");
  const { id } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    fetch(`/restaurants/${id}`)
      .then((r) => {
        if (r.ok) {
          return r.json();
        } else {
          throw new Error(`Error fetching restaurant: ${r.status}`);
        }
      })
      .then((data) => {
        setRestaurant(data);
        setStatus("resolved");
        setError(null);
      })
      .catch((err) => {
        setError(err.message);
        setStatus("rejected");
      });
  }, [id]);

  // Function to handle restaurant deletion
  const handleDeleteRestaurant = () => {
    fetch(`/restaurants/${id}`, {
      method: "DELETE",
    })
      .then((r) => {
        if (r.ok) {
          navigate("/restaurants"); // Redirect to the restaurants list after deletion
        } else {
          throw new Error(`Error deleting restaurant: ${r.status}`);
        }
      })
      .catch((err) => {
        setError(err.message);
        setStatus("rejected");
      });
  };

  if (status === "pending") return <h1>Loading...</h1>;
  if (status === "rejected") return <h1>Error: {error}</h1>;

  return (
    <section>
      <h2>{restaurant.name}</h2>
      <h2>{restaurant.address}</h2>

      <h3>Pizzas:</h3>
      <ul>
        {/* {restaurant.pizzas.map((pizza) => (
          <li key={pizza.id}>
            <Link to={`/pizzas/${pizza.id}`}>{pizza.name}</Link>
          </li>
        ))} */}
      </ul>

      <button onClick={handleDeleteRestaurant}>Delete Restaurant</button>
    </section>
  );
}

export default Restaurant;
