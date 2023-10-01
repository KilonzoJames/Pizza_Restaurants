import React from 'react'
import { Route, Routes } from "react-router-dom";
import Header from './Header';
import Home from './Home';
import Restaurant from './Restaurant';
import RestaurantPizza from './RestaurantPizza';

function App() {
  return (
    <div>
        <Header />
        <main>
          <Routes>
            <Route path="/" exact element={<Home />} />
            <Route path='/restaurants/:id' element={<Restaurant/>} />
            <Route path='/restaurant_pizzas' element={<RestaurantPizza/>} />
          </Routes>
        </main>
    </div>
  )
}

export default App
